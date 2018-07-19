# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 1:26
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : urls.py
# @Software: PyCharm# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from .views import CourseList,CourseDetailView,CourseJoin,LessonJoin
from django.conf.urls.static import static
from FITA import settings
urlpatterns = [
    # 课程列表页
    url(r'^$', CourseList.as_view(), name='course_list'),
    # 课程详细页
    url(r'detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name='course_detail'),
    #报名课程
    url(r'detail/(?P<course_id>\d+)/course_join_ajax',CourseJoin.as_view(),name='course_join'),
    #参与对应的线下活动
    url(r'detail/(?P<course_id>\d+)/lesson_join_ajax', LessonJoin.as_view(), name='lesson_join')
    # 章节详细页
    # url(r'^info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    # # 课程评论
    # url(r'^comment/(?P<course_id>\d+)/', CommentView.as_view(), name='course_comment'),
    # # 添加课程评论
    # url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)