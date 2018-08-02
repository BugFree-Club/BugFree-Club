# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 23:28
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import *
from operations.models import MemberApplication,Contact


class MemberApplicationAdmin(object):
    list_display = ['user','is_passed','add_time']
    search_fields = ['user']
    list_filter = ['is_passed','add_time']


xadmin.site.register(MemberApplication, MemberApplicationAdmin)


class ContactAdmin(object):
    list_display = ['user','des']
    list_filter = ['add_time']


xadmin.site.register(Contact, ContactAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'add_time']
    search_fields = ['title', 'image', 'add_time']
    list_filter = ['title', 'image', 'add_time']


xadmin.site.register(Banner, BannerAdmin)


class IndexCourseAdmin(object):
    list_display = ['course_name']


xadmin.site.register(IndexCourse, IndexCourseAdmin)


class IndexImgShowAdmin(object):
    list_display = ['image_name','is_shown']
    list_filter = ['is_shown']


xadmin.site.register(IndexImgShow,IndexImgShowAdmin)


class IndexCoreMembersAdmin(object):
    list_display = ['name','is_shown']
    list_filter = ['is_shown']


xadmin.site.register(IndexCoreMembers,IndexCoreMembersAdmin)


class IndexHonorWallAdmin(object):
    list_display = ['name', 'is_shown']
    list_filter = ['is_shown']


xadmin.site.register(IndexHonorWall,IndexHonorWallAdmin)
