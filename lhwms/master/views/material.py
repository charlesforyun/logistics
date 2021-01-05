import json
import datetime
import re

from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST

from master.models import *

from lhwms import operator
from lhwms.operator import reader
from lhwms.operator import importer

from .common import export_fields
from .common import import_fields
from .common import change
from .common import join_fields

from master.errors import *
from log.views import errlog

from django.db import connection
from django.db import transaction

MASTER_MODEL = Material
MASTER_NAME = '物料'


# @cache_page(12 * 3600)
def material(request):
    '''加载物料管理页面'''
    try:
        return render(request, 'material.html')

    except Exception as e:
        errlog.errlog_add(request, str(e))
        return HttpResponse(str(e))


def search_data(request):
    '''根据条件查询数据'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        check_acc = False
        fun_check = None
        where = None
        joins = join_fields[MASTER_MODEL.__name__]

        reader.search(request, model, query_mark, request.POST,
                      check_acc, fun_check, where, joins)

        msg = '操作成功！已成功执行数据查询操作。'
        info_back = {'type': 1, 'msg': msg}

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}

    finally:
        return HttpResponse(json.dumps(info_back))


def load_data(request):
    '''获取分页数据'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        page_num = int(request.GET['page'])
        row_num = int(request.GET['rows'])
        joins = join_fields[MASTER_MODEL.__name__]

        data = reader.load(request, model, query_mark, page_num, row_num, joins)
        return HttpResponse(data)

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


def export_excel(request):
    '''导出EXCEL'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        fields_export = export_fields[MASTER_MODEL.__name__]
        joins = join_fields[MASTER_MODEL.__name__]

        response = reader.export_excel(request, model, query_mark,
                                       fields_export, joins)
        return response

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


@require_POST
def upload_excel(request):
    '''上传EXCEL导入物料数据'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        file = request.FILES.get('file_upload')
        fields_import = import_fields[MASTER_MODEL.__name__]
        joins = join_fields[MASTER_MODEL.__name__]

        result = importer.read_excel(request, model, query_mark,
                                     file, fields_import, joins)
        return HttpResponse(result)

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


@require_POST
def import_data(request):
    '''执行物料数据导入'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        fields_import = import_fields[MASTER_MODEL.__name__]

        res = importer.import_rows(request, model, query_mark, fields_import)

        context = (MASTER_NAME, res['insert'], MASTER_NAME, res['update'])
        msg = '操作成功！新增%s %d 个，更新%s %d 个。' % context
        info_back = {'type': 1, 'msg': msg}

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}

    finally:
        return HttpResponse(json.dumps(info_back))


def down_excel_template(request):
    '''下载EXCEL数据导入模板'''
    try:
        fields_import = import_fields[MASTER_MODEL.__name__]
        response = importer.get_template(request, fields_import)
        return response

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


@require_POST
def delete(request):
    '''删除物料'''
    response = change(request, MASTER_MODEL, 'is_visible', False, '删除',
                      MASTER_NAME)
    return response


@require_POST
def allow(request):
    '''启用物料'''
    response = change(request, MASTER_MODEL, 'is_enable', True, '启用',
                      MASTER_NAME)
    return response


@require_POST
def forbid(request):
    '''禁用物料'''
    response = change(request, MASTER_MODEL, 'is_enable', False, '禁用',
                      MASTER_NAME)
    return response


@require_POST
def clean_querys(request):
    '''清理缓存'''
    try:
        model = MASTER_MODEL
        query_mark = MASTER_NAME
        operator.clean_querys(request, model, query_mark)
        msg = '操作成功！已成功执行缓存清理操作。'
        info_back = {'type': 1, 'msg': msg}

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


@require_POST
def add(request):
    '''新增物料'''
    try:
        rp = request.POST
        # 检查物料名是否重复
        mods = MASTER_MODEL.objects.filter(mat_no=rp['mat_no'], is_visible=True)
        if len(mods):
            raise Material_exist_err
        new_mat = MASTER_MODEL()
        new_mat.mat_no = rp['mat_no']
        new_mat.mat_name = rp['mat_name']
        new_mat.company = rp['company']
        new_mat.work_group = rp['work_group']
        new_mat.contact = rp['contact']
        new_mat.save()
        # 成功信息
        msg = '操作成功！已成功添加物料"%s"。' % new_mat.mat_name
        info_back = {'type': 1, 'msg': msg}
        return HttpResponse(json.dumps(info_back))

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


@require_POST
def edit(request):
    '''修改物料'''
    try:
        rp = request.POST
        # 检查物料工号是否重复
        mods = MASTER_MODEL.objects.filter(mat_no=rp['mat_no'], is_visible=True)
        if len(mods) and int(mods[0].id) != int(rp['id']):
            raise Material_exist_err

        # 写入物料数据
        new_mat = MASTER_MODEL.objects.get(id=rp['id'])
        new_mat.mat_no = rp['mat_no']
        new_mat.mat_name = rp['mat_name']
        new_mat.company = rp['company']
        new_mat.work_group = rp['work_group']
        new_mat.contact = rp['contact']
        new_mat.save()

        # 成功信息
        msg = '操作成功！已成功修改物料"%s"。' % new_mat.mat_name
        info_back = {'type': 1, 'msg': msg}
        return HttpResponse(json.dumps(info_back))

    except Exception as e:
        errlog.errlog_add(request, str(e))
        msg = '操作失败！错误：%s。' % str(e)
        info_back = {'type': 3, 'msg': msg}
        return HttpResponse(json.dumps(info_back))


def lists(request):
    '''获得物料代码列表'''
    try:
        q = request.POST.get('q')
        if not q:
            mats = MASTER_MODEL.objects.filter(is_visible=True, is_enable=True)
        else:
            mats = MASTER_MODEL.objects.filter(mat_name__contains=q,
                                               is_visible=True, is_enable=True)
        li = []
        for p in mats:
            s = {
                'mat_no': p.mat_no,
                'mat_name': p.mat_name,
                'company': p.company,
                'work_group': p.work_group,
            }
            li.append(s)
        return HttpResponse(json.dumps(li))

    except Exception as e:
        errlog.errlog_add(request, str(e))
        return HttpResponse(str(e))
