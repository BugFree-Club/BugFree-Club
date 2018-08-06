from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course,Lesson
from manage_site.models import Preview


# 评论 提问功能未开发
class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户:%s 课程:%s' % (self.user, self.course)


class UserFavourite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '负责人')),default=0, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='接受用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.message)

    def to_read(self):
        self.has_read = True
        self.save()


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.course)


class UserLesson(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='章节',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '用户章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.lesson)

class MemberApplication(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    des = models.TextField(verbose_name='个人简介')
    is_passed = models.BooleanField(verbose_name='审核状态', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '加入申请'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    '''联系我们'''
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    des = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '联系我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class UserAct(models.Model):
    '''活动报名'''
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    activity = models.ForeignKey(Preview,verbose_name='内容',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '活动报名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


