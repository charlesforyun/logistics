from django.db import models


class Basic(models.Model):
    '''表父类'''

    def todict(self):
        dic = self.__dict__
        for key in dic:
            dic[key] = str(dic[key])
        del dic['_state']
        return dic

    def __str__(self):
        return str(self.todict)

    class Meta:
        abstract = True


class Constructor(Basic):
    '''施工单位表'''
    id = models.AutoField(primary_key=True)
    cons_mark = models.CharField(max_length=16, db_index=True)  # 施工单位代码
    cons_name = models.CharField(max_length=32)  # 施工单位名称
    cons_manager = models.CharField(max_length=16, null=True)  # 负责人
    cons_tel = models.CharField(max_length=32, null=True)  # 联系方式
    is_visible = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)


class Warehouse(Basic):
    '''周转库表'''
    id = models.AutoField(primary_key=True)
    cons_mark = models.CharField(max_length=16, db_index=True,
                                 null=True)  # 所属施工单位代码
    wh_mark = models.CharField(max_length=16, db_index=True, null=True)  # 周转库代码
    wh_name = models.CharField(max_length=32)  # 周转库名称
    wh_manager = models.CharField(max_length=16, null=True)  # 仓管员
    wh_tel = models.CharField(max_length=32, null=True)  # 联系方式
    is_visible = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)


class Material(Basic):
    '''物料表'''
    id = models.AutoField(primary_key=True)
    mat_mark = models.CharField(max_length=16, db_index=True)  # 物料编码
    # exp_mark = models.SmallIntegerField(default=0, db_index=True) # 物料扩展码
    mat_type = models.CharField(max_length=32)  # 物资类型
    mat_des = models.CharField(max_length=256, null=True)  # 物料描述
    # exp_class = models.CharField(max_length=256, null=True) # 扩展描述
    unit = models.CharField(max_length=8)  # 计量单位
    min_num = models.FloatField(default=1)  # 最低单位数量
    is_device = models.BooleanField(default=True)  # 是否设备
    is_visible = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)
