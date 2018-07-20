# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FITA.settings")

application = get_wsgi_application()
