from django.shortcuts import render,render_to_response
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from .models import *
from .form import *


class IndexView(FormMixin,View):
    def get(self, request):
        context = {}
        context['img_show_list_1'] =  IndexImgShow.objects.filter(is_shown__exact=True)[0:3]
        context['img_show_list_2'] =  IndexImgShow.objects.filter(is_shown__exact=True)[3:6]
        context['core_member_list'] = IndexCoreMembers.objects.filter(is_shown__exact=True)
        context['honor_wall_list'] = IndexHonorWall.objects.filter(is_shown__exact=True)
        context['banner_list']= Banner.objects.all()
        context['course_list'] = IndexCourse.objects.all()

        return render(request, 'manage_site/index.html',context)


# def page_not_found(request):
#     '''全局404'''
#     return render_to_response('manage_site/404.html')