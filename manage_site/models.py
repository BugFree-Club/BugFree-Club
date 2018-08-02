from django.db import models
from datetime import datetime
from courses.models import Course

class Banner(models.Model):
    '''主页轮播公告功能'''
    title = models.CharField(max_length=100, verbose_name="标题",default='未填')
    details = models.TextField(max_length=500,verbose_name='公告内容',default='未填')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播公告"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.title


class IndexCourse(models.Model):
    '''主页展示的课程'''
    course_name = models.ForeignKey(Course,verbose_name='课程名称',on_delete=models.CASCADE)
    des = models.TextField(max_length=200,verbose_name='简单描述')
    img = models.ImageField(upload_to="manage_site/course/%Y/%m",max_length=200,verbose_name='课程LOGO')

    class Meta:
        verbose_name = "展示课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_name.name



class IndexImgShow(models.Model):
    '''主页精彩照片墙'''
    image = models.ImageField(upload_to='manage_site/img_show/%Y/%d',max_length=100,verbose_name='照片')
    image_name = models.CharField(max_length=20,verbose_name='照片名称',default='精彩瞬间')
    des = models.TextField(max_length=200,verbose_name='照片描述')
    is_shown = models.BooleanField(default=True,verbose_name='是否显示')

    class Meta:
        verbose_name = "照片墙"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image_name


class IndexCoreMembers(models.Model):
    '''主页核心成员'''
    name = models.CharField(max_length=20,verbose_name='核心成员姓名')
    image = models.ImageField(upload_to='manage_site/member/%Y/%d',max_length=100,verbose_name='成员照片')
    postion = models.CharField(max_length=30,verbose_name='担任职位')
    des = models.TextField(max_length=200,verbose_name='简单描述')
    is_shown = models.BooleanField(default=True, verbose_name='是否显示')
    class Meta:
        verbose_name = "核心成员展示"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name







class Preview(models.Model):
    '''主页活动预告'''
    is_shown = models.BooleanField(default=True,verbose_name='首页显示')

    people = models.IntegerField(verbose_name='已报名人数',default=0)
    name = models.CharField(max_length=20, verbose_name='活动名称')
    des = models.TextField(max_length=200, verbose_name='简单描述')
    details = models.TextField(max_length=500,verbose_name='详细信息')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "活动预告"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.name
