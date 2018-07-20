from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserCourse

