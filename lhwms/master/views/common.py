import json
import datetime
import re

from django.http import HttpResponse
from django.http import FileResponse

from master.models import *

from lhwms.operator import *
from lhwms.operator.reader import ExportField
from lhwms.operator.importer import ImportField

from master.errors import *
from log.views import errlog


# 公用函数

def change(request, model, field, value, opname, mname):
    '''修改条目状态通用方法'''
    try:
        # 解析并去重上传的id
        data = json.loads(request.POST['ids'])  # json
        ids = set(data)
        # 修改条目
        for n in ids:
            g = model.objects.get(id=int(n))
            if g is not None:
                setattr(g, field, value)
                g.save()
        # 成功信息
        msg = '操作成功！已成功%s %s 个%s。' % (opname, len(ids), mname)
        info_back = {'type': 1, 'msg': msg}

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}

    finally:
        return HttpResponse(json.dumps(info_back))


# Constructor 施工单位字段集

fields_export_constructor = [
    ExportField('cons_mark', '施工单位代码', 10),
    ExportField('cons_name', '施工单位名称', 40),
    ExportField('cons_manager', '负责人', 10),
    ExportField('cons_tel', '联系方式'),
    ExportField('is_enable', '启用', 10),
]

fields_import_constructor = [
    ImportField('cons_mark', True, False, '施工单位代码', '^(.*){1,16}$'),
    ImportField('cons_name', False, False, '施工单位名称', '^(.*){1,64}$'),
    ImportField('cons_manager', False, True, '负责人', '^(.*){0,16}$'),
    ImportField('cons_tel', False, True, '联系方式', '^(.*){0,32}$'),
]

fields_join_constructor = []

# Warehouse 周转库字段集

fields_export_warehouse = [
    ExportField('wh_mark', '周转库代码', 10),
    ExportField('wh_name', '周转库名称', 15),
    ExportField('cons_manager', '仓管员', 10),
    ExportField('cons_tel', '联系方式'),
    ExportField('cons_mark', '施工单位代码', 10),
    ExportField('cons_name', '施工单位名称', 40),
    ExportField('is_enable', '启用', 10),
]

fields_import_warehouse = [
    ImportField('wh_mark', True, False, '周转库代码', '^(.*){1,16}$'),
    ImportField('wh_name', False, False, '周转库名称', '^(.*){1,32}$'),
    ImportField('wh_manager', False, True, '仓管员', '^(.*){0,16}$'),
    ImportField('wh_tel', False, True, '联系方式', '^(.*){0,32}$'),
    ImportField('cons_mark', False, False, '施工单位代码', '^(.*){1,16}$'),
]

fields_join_warehouse = [
    {
        'join_model': Constructor,
        'join_model_name': '施工单位',
        'fields': [{'from': 'cons_mark', 'to': 'cons_mark'}]
    },
]

# Material 物料字段集


fields_export_material = [
    ExportField('mat_mark', '物料编码', 15),
    ExportField('mat_type', '物资类型', 15),
    ExportField('mat_des', '物料描述', 40),
    ExportField('unit', '计量单位', 10),
    ExportField('min_num', '最低单位数量', 10),
    ExportField('is_device', '是否设备', 10),
    ExportField('is_enable', '启用', 10),
]

fields_import_material = [
    ImportField('mat_mark', True, False, '物料编码', '^(.*){1,16}$'),
    ImportField('mat_type', False, False, '物资类型', '^(.*){1,16}$'),
    ImportField('mat_des', False, False, '物料描述', '^(.*){1,256}$'),
    ImportField('unit', False, False, '计量单位', '^(.*){1,8}$'),
    ImportField('min_num', False, False, '最低单位数量', '^(.*){1,16}$'),
    ImportField('is_device', False, False, '是否设备(0/1)', '^\d+$'),
]

fields_join_material = []

# 导出字段
export_fields = {
    'Warehouse': fields_export_warehouse,
    'Constructor': fields_export_constructor,
    'Material': fields_export_material,
}

# 导入字段
import_fields = {
    'Warehouse': fields_import_warehouse,
    'Constructor': fields_import_constructor,
    'Material': fields_import_material,
}

# 关联字段
join_fields = {
    'Warehouse': fields_join_warehouse,
    'Constructor': fields_join_constructor,
    'Material': fields_join_material,
}
