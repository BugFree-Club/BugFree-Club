from django.shortcuts import render,render_to_response
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect,HttpResponse
from .models import *
from users.form import MemberApplicationForm,ContactForm
from operations.models import MemberApplication,Contact
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request):
        context = {}
        context['img_show_list_1'] =  IndexImgShow.objects.filter(is_shown__exact=True)[0:3]
        context['img_show_list_2'] =  IndexImgShow.objects.filter(is_shown__exact=True)[3:6]
        context['core_member_list'] = IndexCoreMembers.objects.filter(is_shown__exact=True)
        context['honor_wall_list'] = IndexHonorWall.objects.filter(is_shown__exact=True)
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




class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        contactForm = ContactForm()
        return render(request,'manage_site/contact_form_tag.html',locals())
    '''联系我们'''
    def post(self, request):
        user_id = request.user.id
        context = request.POST.get('des','')
        if context is None:
            return HttpResponse('{"status":"failure", "data":"请输入您想要对我们说的话"}', content_type='application/json')
        Contact.objects.create(user_id=user_id, des=context)
        return HttpResponse('{"status":"success", "data":"感谢您的宝贵建议！"}', content_type='application/json')
    #TODO：防止ddos检测post频率