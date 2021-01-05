from django.views.decorators.http import require_POST
from user.models import User
from outgoing.models import OutgoingApply
from lhwms.utils import restful
from lhwms.utils import attachment


@require_POST
def outgoing_apply_create(request):
    """领用申请创建"""
    user = User.objects.get(pk=1)

    stock_mark = request.POST.get('stock_mark')  # 存放编号
    mat_mark = request.POST.get('mat_mark')  # 物料编码
    mat_from = request.POST.get('mat_from')  # 物料描述(选填)
    out_cons_mark = request.POST.get('out_cons_mark')  # 单位
    num = request.POST.get('num')  # 领用数量
    inventory_place = request.POST.get('inventory_place')  # 库存地
    recipient = request.POST.get('recipient')  # 领用人
    use = request.POST.get('use')  # 用途
    use_project = request.POST.get('use_project')  # 使用工程

    outgoing_create_file = OutgoingApply(
        user=user,
        stock_mark=stock_mark,
        mat_mark=mat_mark,
        mat_from=mat_from,
        out_cons_mark=out_cons_mark,
        num=num,
        inventory_place=inventory_place,
        recipient=recipient,
        use=use,
        use_project=use_project,
    )
    outgoing_create_file.save()


@require_POST
def outgoing_apply_delete(request):
    """删除对象"""
    pk = request.POST.get('pk')
    outgoing_delete_file = OutgoingApply.objects.get(pk=1)
    if outgoing_delete_file.is_visible is True or \
            outgoing_delete_file.is_enable is True:
        return restful.ok(data='您无权限执行此操作！该入库单已通过申请或者已提交')
    else:
        outgoing_delete_file.delete()
        return restful.ok(data='改出库申请单已删除！')


@require_POST
def outgoing_apply_update(request):
    """更新对象"""
    pk = request.POST.get('pk')
    outgoing_file = OutgoingApply.objects.filter(pk=pk)

    stock_mark = request.POST.get('stock_mark')  # 存放编号
    mat_mark = request.POST.get('mat_mark')  # 物料编码
    mat_from = request.POST.get('mat_from')  # 物料描述(选填)
    out_cons_mark = request.POST.get('out_cons_mark')  # 单位
    num = request.POST.get('num')  # 领用数量
    inventory_place = request.POST.get('inventory_place')  # 库存地
    recipient = request.POST.get('recipient')  # 领用人
    use = request.POST.get('use')  # 用途
    use_project = request.POST.get('use_project')  # 使用工程

    outgoing_file.update(
        stock_mark=stock_mark,
        mat_mark=mat_mark,
        mat_from=mat_from,
        out_cons_mark=out_cons_mark,
        num=num,
        inventory_place=inventory_place,
        recipient=recipient,
        use=use,
        use_project=use_project,
    )
    return restful.ok(data='更新操作成功！')


@require_POST
def outgoing_apply_submit(request):
    """提交申请"""
    pk = request.POST.get('pk')
    submit_outgoing_apply = OutgoingApply.objects.filter(pk=pk)
    submit_outgoing_apply.update(is_visible=True)
    return restful.ok(data='提交成功！')


@require_POST
def outgoing_apply_approve(request):
    """
    审批和驳回
    :param request: pk,approve,
    :return:
    """
    pk = request.POST.get('pk')
    approve_submit = request.POST.get('approve')
    reject_submit = request.POST.get('reject')
    submit_outgoing_apply = OutgoingApply.objects.filter(pk=pk)

    if approve_submit is True:
        submit_outgoing_apply.update(is_enable=True)
        return restful.ok(data='审批通过')


@require_POST
def outgoing_accessory_uploading(request):
    data = attachment.attachment_uploading(request, model=OutgoingApply)
    return restful.ok(data)


@require_POST
def outgoing_accessory_delete(request):
    data = attachment.attachment_delete(request)
    return restful.ok(data)