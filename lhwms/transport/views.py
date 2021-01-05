from django.views.decorators.http import require_POST
from user.models import User
from transport.models import TransportApply
from lhwms.utils import restful


@require_POST
def transport_apply_create(request):
    """领用申请创建"""
    user = User.objects.get(pk=1)

    stock_mark = request.POST.get('stock_mark')  # 存放编号
    mat_mark = request.POST.get('mat_mark')  # 物料编码
    mat_from = request.POST.get('mat_from')  # 物料描述(选填)
    out_cons_mark = request.POST.get('out_cons_mark')  # 单位
    num = request.POST.get('num')  # 调拨数量
    outgoing_place = request.POST.get('outgoing_place')  # 调出库存地
    incoming_place = request.POST.get('incoming_place')  # 调入库存地
    transport_reason = request.POST.get('transport_reason')  # 调拨理由

    transport_create_file = TransportApply(
        user=user,
        stock_mark=stock_mark,
        mat_mark=mat_mark,
        mat_from=mat_from,
        out_cons_mark=out_cons_mark,
        num=num,
        outgoing_place=outgoing_place,
        incoming_place=incoming_place,
        transport_reason=transport_reason,

    )
    transport_create_file.save()


@require_POST
def transport_apply_delete(request):
    """删除对象"""
    pk = request.POST.get('pk')
    transport_delete_file = TransportApply.objects.get(pk=1)
    if transport_delete_file.is_visible is True or \
            transport_delete_file.is_enable is True:
        return restful.ok(data='您无权限执行此操作！该入库单已通过申请或者已提交')
    else:
        transport_delete_file.delete()
        return restful.ok(data='改出库申请单已删除！')


@require_POST
def transport_apply_update(request):
    """更新对象"""
    pk = request.POST.get('pk')
    transport_file = TransportApply.objects.filter(pk=pk)

    stock_mark = request.POST.get('stock_mark')  # 存放编号
    mat_mark = request.POST.get('mat_mark')  # 物料编码
    mat_from = request.POST.get('mat_from')  # 物料描述(选填)
    out_cons_mark = request.POST.get('out_cons_mark')  # 单位
    num = request.POST.get('num')  # 调拨数量
    outgoing_place = request.POST.get('outgoing_place')  # 调出库存地
    incoming_place = request.POST.get('incoming_place')  # 调入库存地
    transport_reason = request.POST.get('transport_reason')  # 调拨理由

    transport_file.update(
        stock_mark=stock_mark,
        mat_mark=mat_mark,
        mat_from=mat_from,
        out_cons_mark=out_cons_mark,
        num=num,
        outgoing_place=outgoing_place,
        incoming_place=incoming_place,
        transport_reason=transport_reason,
    )
    return restful.ok(data='更新操作成功！')


@require_POST
def transport_apply_submit(request):
    """提交申请"""
    pk = request.POST.get('pk')
    submit_transport_apply = TransportApply.objects.filter(pk=pk)
    submit_transport_apply.update(is_visible=True)
    return restful.ok(data='提交成功！')


@require_POST
def transport_apply_approve(request):
    """
    审批和驳回
    :param request: pk,approve,
    :return:
    """
    pk = request.POST.get('pk')
    approve_submit = request.POST.get('approve')
    reject_submit = request.POST.get('reject')
    submit_transport_apply = TransportApply.objects.filter(pk=pk)

    if approve_submit is True:
        submit_transport_apply.update(is_enable=True)
        return restful.ok(data='审批通过')
