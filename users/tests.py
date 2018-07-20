# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm

from django.test import TestCase
from .models import UserProfile

# Create your tests here.

class UserTest(TestCase):
    def initUser(self):
        for i in range(0,20):
            username = 'test'+str(i)
            password = 'qwertyuiop'
            user = UserProfile.objects.create_user(username=username,password=password)

