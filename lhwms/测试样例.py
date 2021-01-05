'''
六合测试样例
'''
import requests
import json
import os
import datetime
import sys
from log.models import Errlog
from log.views.publicLog import log_print
sys.setrecursionlimit(1000000)

root = 'http://192.168.2.241:8000'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def datagrid_search_load_test():
    '''页面数据列表查询和加载测试'''
    url_search = root + 'master/constructor/search_data'
    url_load = root + 'master/constructor/load_data'

    params = {'cons_name': '聚联'}
    r = requests.post(url_search, data=params)
    # print(r.status_code, r.text)
    params = {'page': '1', 'rows': '50'}
    r = requests.get(url_load, params=params)
    # jr = json.loads(r.text)
    print(r.status_code, r.json())


def allow_forbid_test():
    '''启用/禁用接口测试'''
    url = root + 'master/constructor/allow'

    params = {'ids': '[1, 2]'}
    r = requests.post(url, data=params)
    jr = json.loads(r.text)
    print(r.status_code, jr)


def download_excel_test():
    '''导出数据接口测试'''
    url_search = root + 'master/constructor/search_data'
    url_export = root + 'master/constructor/export_excel'

    params = {'cons_name': ''}
    requests.post(url_search, data=params)

    r = requests.get(url_export)
    filename = os.path.abspath('.') + r'\book.xlsx'
    with open(filename, 'wb') as code:
        code.write(r.content)


def apply_crate_test():
    # (.*?):(.*)   '$1': '$2',
    '''创建申请单测试'''
    url_search = root + 'incoming/apply/accessory/'
    data1 = {
        'pk': 13,
        'incoming_doc_mark': '1',
        'stock_mark': '1',
        'apply_cons_mark': '1',
        'asset_name': '1',
        'proj_from': '',
        'proj_mark': '1',
        'proj_name': '1',
        'ini_from': '1',
        'mat_mark': 'sdfsdf',
        'mat_type': '1',
        'pars': '1',
        'dp': None,
        'supplyer': 'sdfsdf',
        'bp': 'sdfsdfs',
        'use_date': datetime.date(2021, 2, 3),
        'remove_date': datetime.date(2021, 2, 3),
        'pms_status': 'sdfsdfs',
        'test_result': 'sdfsdf',
        'wh_mark': 'sdfsdf',
        'num': 23,
        'mat_extend_mark': 'sdfsdf',
        'mat_from': '345',
        'accessory': '1',
    }
    url = BASE_DIR + '/lhwms/media/1.txt'
    data = {
        'pk': 1,
    }
    r = requests.post(url=url_search, data=data).json()
    # r = requests.get(url=url_search).json()
    print(r)


def apply_update():
    url_search = root + 'incoming/apply/delete/'
    date = {
        'pk': '15',
        'incoming_doc_mark': '2',
        'stock_mark': '14',
        'apply_cons_mark': '14',
        'asset_name': '14',
        'proj_from': '',
        'proj_mark': '1',
        'proj_name': '1',
        'ini_from': '1',
        'mat_mark': 'sdfsdf',
        'mat_type': '1',
        'pars': '1',
        'dp': None,
        'supplyer': 'sdfsdf',
        'bp': 'sdfsdfs',
        'use_date': datetime.date(2021, 2, 3),
        'remove_date': datetime.date(2021, 2, 3),
        'pms_status': 'sdfsdfs',
        'test_result': 'sdfsdf',
        'wh_mark': 'sdfsdf',
        'num': 23,
        'mat_extend_mark': 'sdfsdf',
        'mat_from': '345',
    }
    r = requests.post(url=url_search, data=date).json()
    print(r)


def apply_submit():
    url_search = root + 'incoming/apply/submit/'
    datas = json.dumps({1: 'df', 2: 'ds'})
    date = {
        'pk': datas,
        'name': 'sdf'

    }
    r = requests.post(url=url_search, data=date).json()
    print(r, type(r))


def apply_show():
    # 数据是分页展示
    url_serach = root + 'incoming/apply/creator/'
    r = requests.get(url=url_serach, params={
        'page': '1'
    }).json()
    print(r)


def apply_search():
    # 数据条件查询
    # url_serach = root + '/incoming/apply/search/'
    url_serach = root + '/log/errlog/search_data'
    data = {
        'terms': json.dumps({'id': 79}),
        'page': 2
            }
    r = requests.post(url=url_serach, data=data).json()
    print(r)


def apply_paginator():
    # 数据条件查询
    url_serach = root + 'incoming/apply/paginator/'
    data = {
        'page': 2
            }
    r = requests.get(url=url_serach, params=data).json()
    print(r)


if __name__ == '__main__':
    pass
    # apply_show()
    # apply_search()
    # apply_paginator()
    # log_print('cuowu')

