from functools import wraps
from django.shortcuts import redirect, reverse
from apps.logistics_auth.models import User


def login_required(func):
    """
    decorator for get user's '_auth_user_id';
    :return: func() or login_view 判断是否存在用户登录，没有就返回登陆页面
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # user = request.session.get('_auth_user_id')
        # exist = User.objects.filter(pk=user).exists()
        if request.front_user:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('bank:login'))

    return wrapper
