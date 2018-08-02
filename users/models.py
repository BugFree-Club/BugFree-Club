# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from FITA.settings import DEP_CHOICE,PROVINCE




class UserProfile(AbstractUser):
    gender = models.CharField(choices=(("Male", "男"), ("female", "女")), max_length=6, verbose_name='性别')
    address = models.CharField(choices=PROVINCE,max_length=5, default='wt', verbose_name='省份')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    department = models.CharField(choices=DEP_CHOICE,default='z',verbose_name='学院',max_length=20)
    image = models.ImageField(upload_to="users/%Y/%m", default="/users/default.png", max_length=100,verbose_name='头像')
    is_member = models.BooleanField(default=False, verbose_name='是否成员')

    class Meta:
        verbose_name = " 用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")),
                                 max_length=10, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


edu_situation = (
    (u'未填', u'未填'), (u'大一', u'大一'), (u'大二', u'大二'),
    (u'大三', u'大三'), (u'大四', u'大四'), (u'大五', u'大五'),
    (u'研一',u'研一'), (u'研二', u'研二'), (u'研三', u'研三')
)

class Teacher(models.Model):
    name = models.ForeignKey(UserProfile,verbose_name="负责人姓名", on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='users/teachers/%Y/%m', verbose_name='负责人照片', default='/users/teacher/default.png')
    edu_bak = models.CharField(verbose_name='当前学历', choices=edu_situation, default=u'未填', max_length=50)
    teacher_info = models.CharField(max_length=200, verbose_name="个人信息")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数目")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    class Meta:
        verbose_name = "负责人"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name.username

