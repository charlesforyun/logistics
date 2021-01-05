import requests
from tempfile import TemporaryFile
import json
import os
import xlrd, xlwt, openpyxl, time

root = 'http://127.0.0.1:8001/'


def login_test():
    url = root + 'school/'
    params = {'15720618047', '123456'}
    r = requests.post(url=url).json()
    print(r)


def excel_read():
    urls = r'E:/python_project/logistics/media/不合格台账.xlsx'
    with xlrd.open_workbook(urls) as workbook:
        print(time.process_time())
        sheetName = workbook.sheet_by_index(0)
        print(sheetName.name, sheetName.nrows, sheetName.ncols)
        for i in range(1, sheetName.nrows):
            print(sheetName.row_values(i))
    a = {1: 2, 3: 4}
    print(type(a))


def excel_write():
    filename = r'E:/python_project/logistics/media/append.xlsx'
    workbook = openpyxl.Workbook()  # 新建工作蒲
    workbooks = workbook.active
    sheet = workbook.create_sheet('append')  # 新增sheet表
    workbooks.append([1, 2, 3])
    workbook.save(filename)


login_test()




