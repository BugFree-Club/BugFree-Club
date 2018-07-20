# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm

from datetime import datetime
from django.db import models
from users.models import Teacher,UserProfile


class Course(models.Model):
    '''课程'''
    name = models.CharField(max_length=50, verbose_name="课程名")
    description = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")  # TODO:暂时定义成textfield, 后续会改为支持富文本的类型
    degree = models.CharField(choices=((u"初级", "初级"), (u"中级", "中级"), (u"高级", "高级")), max_length=2,verbose_name='难度')
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='负责人')

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name
        ordering = ['-click_nums']

    def __str__(self):
        return self.name


class Lesson(models.Model):
    '''课程各个章节'''
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='负责人')

    stu_num = models.IntegerField(default=0, verbose_name="报名人数")
    name = models.CharField(max_length=100, verbose_name="章节名")
    start_time = models.DateTimeField(verbose_name="开始时间")
    last_time = models.IntegerField(default=0, verbose_name="持续时间（小时）")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    classroom = models.CharField(verbose_name='交流地点', default='待定', max_length=100)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name
        ordering = ['-start_time']

    def __str__(self):
        return self.name
