# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 23:28
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import EmailVerifyRecord,Teacher


class EmailVerifyRecordAdmin(object):
    list_display =['code','email','send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']

class TeacherAdmin(object):
    list_display = ['name', 'edu_bak', 'click_num','fav_nums','add_time']
    search_fields = ['name']
    list_filter = ['name', 'edu_bak', 'click_num','fav_nums','add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
