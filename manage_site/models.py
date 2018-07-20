from django.db import models
from datetime import datetime
from courses.models import Course

class Banner(models.Model):
    '''主页轮播图功能'''
    title = models.CharField(max_length=100, verbose_name="标题")  # 轮播图标题
    image = models.ImageField(upload_to="manage_site/banner/%Y/%m", verbose_name="轮播图", max_length=100)  # 轮播图图像地址
   #url = models.URLField(max_length=200, verbose_name="访问地址",blank=True,null=True)  # 轮播图的url
    index = models.IntegerField(default=100, verbose_name="显示顺序")  # 轮播图的显示顺序编号
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")  # 轮播图添加时间

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

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
    image = models.ImageField(upload_to='manage_site/member/%Y/%',max_length=100,verbose_name='成员照片')
    postion = models.CharField(max_length=30,verbose_name='担任职位')
    des = models.TextField(max_length=200,verbose_name='简单描述')
    is_shown = models.BooleanField(default=True, verbose_name='是否显示')
    class Meta:
        verbose_name = "核心成员展示"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class IndexHonorWall(models.Model):
    '''主页荣誉墙'''
    name = models.CharField(max_length=20, verbose_name='荣誉名称')
    des = models.TextField(max_length=200, verbose_name='简单描述')
    is_shown = models.BooleanField(default=True, verbose_name='是否显示')

    class Meta:
        verbose_name = "荣誉墙"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
