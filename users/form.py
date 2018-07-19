# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 0:15
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : form.py
# @Software: PyCharm

from users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ['username','email','gender']


class LoginForm(forms.Form):
    username = forms.CharField(required=True,label='用户名')
    password = forms.CharField(required=True, min_length=5,label='密码')


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True,label='您的邮箱')


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5,label='新的密码')
    password2 = forms.CharField(required=True, min_length=5,label='确认密码')


#
# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''修改个人信息的表单'''
    class Meta:
        model = UserProfile
        fields = ['address', 'image', 'email','gender','address','department','image']


