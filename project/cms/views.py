from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        current_namespace = request.resolver_match.namespace  # 获取当前实例命名空间
        return redirect(reverse("%s:login" % current_namespace))


def reverse1(request):
    re = request.GET.get('name')
    if re:
        return HttpResponse('登陆页面：%s' % re)
    else:
        reverse1_namespace = request.resolver_match.namespace
        print(reverse1_namespace)
        bug = reverse('%s:reverse' % reverse1_namespace, kwargs={"nian": 2014, "yue": 12})
        print(bug)
        return redirect(bug)


def login(request):
        return HttpResponse('CMS登陆页面')


def reverse2(request, nian, yue):
    return HttpResponse('reverse')
