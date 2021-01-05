from apps.logistics_auth.models import User


def frontuser(request):
    """
    获取session信息
    :param request:
    :return:
    """
    user_id = request.session.get('uuid')
    front_user = User.objects.filter(pk=user_id)
    context = {}
    if front_user:
        context['frontuser'] = fron_tuser
        return context
    else:
        return context