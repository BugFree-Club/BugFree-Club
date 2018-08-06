from django.shortcuts import render,render_to_response
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect,HttpResponse
from .models import *
from users.form import MemberApplicationForm,ContactForm
from operations.models import MemberApplication,Contact,UserAct
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request):
        context = {}
        context['img_show_list'] = IndexImgShow.objects.filter(is_shown__exact=True)
        context['core_member_list'] = IndexCoreMembers.objects.filter(is_shown__exact=True)
        context['pre_list'] = Preview.objects.filter(is_shown__exact=True)
        context['banner_list']= Banner.objects.all()
        context['course_list'] = IndexCourse.objects.all()
        context['memberApplicationForm'] = MemberApplicationForm()
        context['contactForm'] = ContactForm()
        return render(request, 'manage_site/index.html', context)



class ApplicationView(LoginRequiredMixin, View):
    '''用户申请加入社团'''
    def post(self, request):
        user_id = request.user.id
        context = request.POST.get('context','')
        try:
            record = MemberApplication.objects.get(user_id=user_id)
        except Exception:
            record = None
        if record:
            if record.is_passed:
                return HttpResponse('{"status":"failure", "data":"您已经是社团成员了！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failure", "data":"请勿重复报名！请等待处理结果"}', content_type='application/json')
        if context is None:
            return HttpResponse('{"status":"failure", "data":"请输入您的报名申请"}', content_type='application/json')
        application_record = MemberApplication.objects.create(user_id=user_id,des=context)
        return HttpResponse('{"status":"success", "data":"报名成功"}', content_type='application/json')




class ActJoinView(LoginRequiredMixin,View):
    '''用户报名'''
    def get(self,request,act_id):
        act = Preview.objects.get(id=act_id)
        return render(request, 'manage_site/activities.html',locals())
    def post(self,request,act_id):
        user_id = request.user.id
        record = UserAct.objects.filter(user_id=user_id, activity_id=act_id)
        if record:
            return HttpResponse('{"status":"fail", "data":"您已经报过名了"}', content_type='application/json')

        UserAct.objects.create(user_id=user_id,activity_id=act_id)
        act = Preview.objects.get(id=act_id)
        act.people += 1
        act.save()

        return HttpResponse('{"status":"success", "data":"报名成功"}', content_type='application/json')




class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        contactForm = ContactForm()
        return render(request,'manage_site/contact_form_tag.html',locals())
    #TODO:对于是否login要考虑 bug!
    '''联系我们'''
    def post(self, request):
        user_id = request.user.id
        context = request.POST.get('des','')
        if context is None:
            return HttpResponse('{"status":"failure", "data":"请输入您想要对我们说的话"}', content_type='application/json')
        Contact.objects.create(user_id=user_id, des=context)
        return HttpResponse('{"status":"success", "data":"感谢您的宝贵建议！"}', content_type='application/json')
    #TODO：防止ddos检测post频率