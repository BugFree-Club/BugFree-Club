# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 1:14
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'(?P<user_id>\d+)/$', UserCenterView.as_view(), name='user_info'),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^forget/$', ForgetPasswordView.as_view(), name='forget'),
    url(r'^reset/(?P<active_code>.*)/$', ResetPasswordView.as_view(), name='reset'),
    url(r'^(?P<user_id>\d+)/changeImg', ImgChangeApi.as_view(), name='change_img')
]