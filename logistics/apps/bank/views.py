from django.views import View
from django.shortcuts import render
from apps.logistics_auth.models import User


def register_view(request):
    print(User.objects.filter(telephone='15720618047'))
    # login(request, user)
    print(request.session.items())
    # dict_items([('_auth_user_id', 'E8aHp3q5hesSGJxEjtfdQv'),

    return render(request, template_name='index/register.html')


def login_view(request):
    print(request.session.items())
    return render(request, template_name='index/login.html')


class Transfer(View):
    def get(self, request):
        pass

    def post(self, request):
        pass



