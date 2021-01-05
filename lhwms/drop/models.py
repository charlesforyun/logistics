from django.db import models


class DropApply(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)

    stock_mark = models.CharField(max_length=16, null=True)  # 存放编号
    mat_mark = models.CharField(max_length=16)  # 物料编码
    mat_from = models.CharField(max_length=64, null=True)  # 物料描述(选填)
    out_cons_mark = models.CharField(max_length=16, db_index=True)  # 单位
    num = models.DecimalField(max_digits=12, decimal_places=3)  # 报废数量
    inventory_place = models.CharField(max_length=16)  # 库存地
    drop_reason = models.CharField(max_length=32)  # 报废理由

    is_visible = models.BooleanField(default=False)  # 提交后可见
    is_enable = models.BooleanField(default=False)  # 申请通过
    is_approve_reason = models.CharField(max_length=32, null=True)  # 驳回理由

    create_time = models.DateField(auto_now_add=True)  # 创建时间
