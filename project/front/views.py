from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
# Create your views here.


def index(request):
    """如果没有登陆用户名，跳转登陆页面"""
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        # reverse('login'） == /signin
        # return redirect('/signin/')
        # 先重定向（redirect（））再反转（reverse（））
        return redirect(reverse('front:login'))


def login(request):
    return HttpResponse('前台登陆页面')
