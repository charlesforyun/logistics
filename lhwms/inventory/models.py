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


class Inventory(Basic):
    '''库存明细表'''
    id = models.AutoField(primary_key=True)

    stock_mark = models.CharField(max_length=16, null=True)  # 存放编号
    apply_cons_mark = models.CharField(max_length=16, db_index=True)  # 申请施工单位代码

    mat_mark = models.CharField(max_length=16)  # 物料编码
    pars = models.CharField(max_length=32)      # 规格型号

    wh_mark = models.CharField(max_length=16)   # 仓库代码
    num = models.DecimalField(max_digits=12, decimal_places=3)  # 数量

    test_result = models.CharField(max_length=16)   # 试验结果
    
    is_visible = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)