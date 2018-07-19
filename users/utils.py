# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 23:00
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : utils.py
# @Software: PyCharm

from django.core.mail import send_mail
from FITA.settings import EMAIL_FROM
from users.models import EmailVerifyRecord
from FITA import settings
import random


def random_str(num):
    code = ''
    for i in range(num):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(add)
    return code


def send_my_email(email, send_type='register'):
    '''用于发送邮件的函数'''

    #数据库中生产一条激活码
    email_record = EmailVerifyRecord()
    email_record.code = random_str(16)
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = "您正在" + settings.COMMUNITY_NAME + "进行注册"
        email_body = "点击下面链接激活账号:" + settings.COMMUNITY_DOMAIN + "/users/active/{0}".format(email_record.code)
    if send_type == "forget":
        email_title = "您正在"+settings.COMMUNITY_NAME+"找回密码"
        email_body = "点击下面链接找回密码:"+settings.COMMUNITY_DOMAIN+"/users/reset/{0}".format(email_record.code)
    else:
        return False
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        return True
    return False
