# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from extra_apps import xadmin
from manage_site.views import IndexView,ApplicationView,ContactView
from django.conf.urls.static import static
from . import settings
#todo:全局404
urlpatterns = [
    path('admin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^application/$', ApplicationView.as_view(), name='application'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url('^users/', include('users.urls')),
    url(r'courses/', include('courses.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
