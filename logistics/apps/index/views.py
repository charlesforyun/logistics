from django.shortcuts import render
from django.core.cache import cache
import memcache
from apps.logistics_auth.decorators import login_required
from django.contrib.auth import login, authenticate
from apps.logistics_auth.models import User


def index_view(request):
    # user = authenticate(telephone='15720618048', password='123456')
    # # user.is_active = False
    # # user.save()
    # print(user)
    # user = User.objects.get(telephone=15720618047)  # 上下文处理器直接获得user对象
    # # login(request, user)
    # print(request.session.items())
    a = cache.set('a', 'dengping')
    # mc = memcache.Client(['127.0.0.1:11211'], debug=True)
    # mc.set('abc', 'dsf')
    print(cache.get('a'), )
    return render(request, template_name='index/index.html')


def register_view(request):
    # print(User.objects.filter(telephone='15720618047'))
    # # login(request, user)
    # print(request.session.items())
    # dict_items([('_auth_user_id', 'E8aHp3q5hesSGJxEjtfdQv'),
    return render(request, template_name='index/register.html')


def login_view(request):
    # print(request.session.items())
    return render(request, template_name='index/login.html')


def memcached_view(request):
    pass
