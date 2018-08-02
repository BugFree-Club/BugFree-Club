# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:36
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @Software: PyCharm

import json
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,reverse,Http404
from django.views.generic import *
from .form import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from operations.models import UserCourse
from .models import UserProfile,EmailVerifyRecord
from .utils import send_my_email



class LoginView(View):
    '''登陆页面'''
    def get(self,requset):
        return render(requset,'users/login.html',{'LoginForm':LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username, password=password)
            print(username,password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                err_msg = '用户账户或密码错误'
        else:
            err_msg = '输入有误，请重试'
        return render(request,'users/login.html',{'err_msg':err_msg,'LoginForm':LoginForm()})


class RegisterView(View):
    '''注册页面'''
    def get(self,requset):
        return render(requset,'users/register.html',{'RegisterForm': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            genger = form.cleaned_data['gender']
            username = form.cleaned_data['username']

            if UserProfile.objects.all().filter(email=email):
                err_msg = '邮箱已存在'
                return render(request,'users/register.html',locals())
            else:
                UserProfile.objects.create_user(username=username,
                                                email=email,
                                                password=password,
                                                gender=genger,)
                return HttpResponseRedirect(reverse('index'))
        else:
            form = RegisterForm(initial={
                'username':request.POST.get('username', ''),
                'email':request.POST.get('email', ''),
                'gender':request.POST.get('gender', '')
            })

            return render(request, 'users/register.html',{'err_msg': '两次密码不相同，请重新输入', 'RegisterForm': form})


class LogoutView(View):
    '''注销'''
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class UserCenterView(LoginRequiredMixin,View):
    '''个人中心页面'''
    def get(self, request, user_id):
        user_id = int(user_id)
        try:
            # 个人信息
            user_info = UserProfile.objects.get(id=user_id)
            # 加入的课程
            all_course = UserCourse.objects.filter(user_id=user_id)
            #表单预填充
            user_info_form = UserInfoForm(initial={
                'email':user_info.email,
                'address':user_info.address,
                'department':user_info.department,
                'gender':user_info.gender,
            })
        except Exception:
            pass
        return render(request, 'users/user_center.html', locals())

    def post(self, request,user_id):
        '''用户信息AJAX提交处理'''
        post_user = request.user
        target_user = UserProfile.objects.get(id=user_id)
        msg = {"status": "failure", "data": "-1"} #默认-1  没有权限操作

        #1.验证是否本人
        if(target_user == post_user) is not True:
            return HttpResponse(json.dumps(msg), content_type='application/json')

        #2.修改个人信息
        user_info_form = UserInfoForm(request.POST, request.FILES, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            msg['data'] = 0 #0表示修改成功
            msg['status'] = 'success'
        else:
            msg['data'] = '1' # 1表示数据不符合规范
        return HttpResponse(json.dumps(msg), content_type='application/json')


class UserDetailView(DetailView):
    model = UserProfile
    context_object_name = 'user_info'
    template_name = 'users/user_info.html'


class ForgetPasswordView(View):
    def get(self, request):
        email_form = ForgetForm()
        return render(request, 'users/pwd_forget.html', locals())

    def post(self,request):
        email_form = ForgetForm(request.POST)
        if email_form.is_valid():
            email = request.POST.get('email', '')
            if send_my_email(email, 'forget'):
                return HttpResponse('{"status":"success", "data":"验证码已经发送，请注意查收"}', content_type='application/json')
        return HttpResponse('{"status":"failure", "data":"发送失败，请稍后再试"}', content_type='application/json')


class ResetPasswordView(View):
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.get(code=active_code)
        if record:
            email = record.email
            modify_form = ModifyPwdForm()
            return render(request, 'users/pwd_reset.html',locals())
        return render(request,'manage_site/index.html')

    def post(self, request, active_code):
        record = EmailVerifyRecord.objects.get(code=active_code)
        modify_forms = ModifyPwdForm(request.POST)
        if modify_forms.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = record.email
            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return HttpResponseRedirect(reverse('login'))
        msg = {'err_msg': '两次密码输入不一致'}
        modify_form = ModifyPwdForm()
        return render(request, "users/pwd_reset.html", locals())


class ImgChangeApi(View):
    def post(self, request,user_id):
        user_img = request.FILES
        print(user_img)

