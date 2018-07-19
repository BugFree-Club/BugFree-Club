# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,View
from .models import Course,Teacher,Lesson
from django.contrib.auth.mixins import LoginRequiredMixin
from operations.models import UserCourse,CourseComments,UserFavourite,UserLesson
# Create your views here.

#TODO:添加搜索功能
class CourseList(View):
    def get(self,request):
        course_list = Course.objects.all()

        paginator = Paginator(course_list, 2)
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            print(page)
            course_list = paginator.page(page)
        except PageNotAnInteger:
            course_list = paginator.page(1)
        except EmptyPage:
            course_list = paginator.page(paginator.num_pages)
        return render(request, 'courses/courses.html', locals())



class CourseDetailView(View):
    def get(self, request, course_id):
        course_has_fav = False
        course_org_has_fav = False
        '''课程点击量+1'''
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        '''负责人点击量+1'''
        teacher = Teacher.objects.get(id=course.teacher.id)
        teacher.click_num += 1
        teacher.save()

        '''课程章节信息'''
        lesson_list_history = Lesson.objects.filter(course_id=course_id, start_time__lt=datetime.now())
        lesson_list_future = Lesson.objects.filter(course_id=course_id, start_time__gt=datetime.now())
        return render(request, 'courses/detail.html', locals())


class CourseJoin(LoginRequiredMixin, View):
    '''用户加入课程'''
    def post(self, request, course_id):
       try:
           if(UserCourse.objects.filter(user=request.user,course_id=course_id)):
               return HttpResponse('{"status":"failure", "data":"您已经加入过该课程了"}', content_type='application/json')
           user_course = UserCourse.objects.create(user=request.user,course_id=course_id)
           add_course = Course.objects.get(id=course_id)
           add_course.students += 1
           add_course.save()
       except Exception as e:
           print(e)
           return HttpResponse('{"status":"failure", "data":"加入失败，请稍后再试"}', content_type='application/json')
       return HttpResponse('{"status":"success", "data":"加入成功"}', content_type='application/json')


class LessonJoin(LoginRequiredMixin, View):
    '''用户报名线下活动'''
    def post(self, request, course_id):
        user_id = request.POST.get('user_id','')
        lesson_id = request.POST.get('lesson_id','')
        if UserLesson.objects.filter(user_id=user_id, lesson_id=lesson_id):
            return HttpResponse('{"status":"failure", "data":"您已经报名了"}', content_type='application/json')
        lesson_record = UserLesson.objects.create(user_id=user_id,lesson_id=lesson_id)
        target_lesson = Lesson.objects.get(id=lesson_id)
        target_lesson.stu_num += 1
        target_lesson.save()

        UserCourse.objects.get_or_create(user=request.user, course_id=course_id)

        return HttpResponse('{"status":"success", "data":"报名成功"}', content_type='application/json')
