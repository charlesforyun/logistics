from apps.logistics_auth.models import User
from django.views.decorators.http import require_POST
from apps.logistics_auth.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from apps.utils import restful


@require_POST
def register_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(
            telephone=telephone, username=username,
            email=email, password=password
        )
        return restful.ok(data='注册成功！')
    else:
        errors = form.get_errors()
        # return redirect(reverse('bank:register'))
        return restful.params_error(message=errors)


@require_POST
def login_view(request):
    """
    表单验证-用户验证-is_active验证-remember
    :param request:
    :return: restful api:json:{"code": 200, "message": "", "data": {}}
    """
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(telephone=telephone, password=password)  # user验证
        if user:
            login(request, user)  # user登陆
            if remember:
                request.session.set_expiry(None)  # default 2周
                return restful.ok(data='缓存时间为2周')
            else:
                request.session.set_expiry(0)  # 设置存留时间为0，退出就清除
                return restful.ok(data='不保留缓存')

        else:
            return restful.un_auth(message='用户不存在，请确认好重新输入！')
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)


def logout_view(request):
    logout(request)
    # request.session.flush()
    return restful.ok(data="已退出登陆！")
