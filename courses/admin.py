# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm

import xadmin
from courses.models import Course,Lesson


class CourseAdmin(object):
    list_display = ['name', 'degree', 'students', 'fav_nums','click_nums', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'degree', 'students', 'fav_nums','click_nums', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)