from django.views import View
import json
from django.views.generic import ListView
from django.shortcuts import render
from apps.utils import restful
from django.core.paginator import Paginator, Page
from django.http import HttpResponse, FileResponse
from django.db import connection
from django.db.models import F, Q, Avg, Sum, Count
from django.db.models.manager import Manager
from apps.school.models import Student, Course, Teacher, Score, Excel
import xlrd, xlwt, openpyxl


class EnterScore(View):

    def get(self, request):
        return render(request, 'shcool/entersocre.html')

    def post(self, request):
        # 成绩统计
        score_form = Student.objects.annotate(
            chinese=Sum('score__number', filter=Q(score__course__name='语文')),
            math=Sum('score__number', filter=Q(score__course__name='数学')),
            english=Sum('score__number', filter=Q(score__course__name='英语')),
            sum=Sum('score__number'),
        ).values("id", "name", "class_name", "chinese", "math", "english",
                 "sum")
        a = Student.objects.get(pk=1)
        b = Student.objects.filter(pk=1)
        print(type(a), type(b))
        print(a.__dict__)
        return restful.ok(data=list(score_form))


class ShowList(View):
    """实现分页"""
    def get(self, request):
        page = int(request.GET.get('page'))
        paginator_page = 20  # 每页需要展示的数据个数
        num = 1  # 需要两边展示的页码数量

        score_form = Student.objects.annotate(
            chinese=Sum('score__number', filter=Q(score__course__name='语文')),
            math=Sum('score__number', filter=Q(score__course__name='数学')),
            english=Sum('score__number', filter=Q(score__course__name='英语')),
            sum=Sum('score__number'),
        ).values("id", "name", "class_name", "chinese", "math", "english",
                 "sum").order_by('id')

        paginator = Paginator(score_form, paginator_page)  # 数据分组
        print(paginator, score_form)
        data_sum = paginator.count  # 所有数据个数
        page_sum = paginator.num_pages  # 所有数据页数
        current_page_data = paginator.page(page)  # 获取当前页数据
        has_next_page = current_page_data.has_next()  # 是否有下一页
        has_previous_page = current_page_data.has_previous()  # 是否有上一页

        if page <= page_sum-num-2:
            """判断左右两边存在合并情况"""
            right_has_more = True  # 1...234..
            right_pages = range(page+1, page+num+1)
        else:
            """89, 789格式"""
            right_has_more = False
            right_pages = range(page+1, page_sum+1)

        if page >= num+3:
            """...234...12"""
            left_has_more = True
            left_pages = range(page-num, page)
        else:
            left_has_more = False
            left_pages = range(1, page)

        if page != 1:
            previous_page_number = current_page_data.previous_page_number()
        else:
            previous_page_number = 1

        if page != page_sum:
            next_page_number = current_page_data.next_page_number()
        else:
            next_page_number = page_sum

        # next_page_number = current_page_data.next_page_number()

        data = {
            'scores': current_page_data,
            'current_page': page,
            'data_sum': data_sum,
            'page_sum': page_sum,
            'has_next': has_next_page,  # 是否存在下一页
            'has_previous': has_previous_page,
            'right_pages': right_pages,
            'left_pages': left_pages,
            'previous_page_number': previous_page_number,  # 点击上一页返回页面id
            'next_page_number': next_page_number,  # 点击下一页返回页面id
            'right_has_more': right_has_more,
            'left_has_more': left_has_more,
        }

        return render(request, 'shcool/showlist.html', context=data)


def excel_write(request):
    """表格按行写入"""
    filename = r'E:/python_project/logistics/media/name.xlsx'
    workbook = openpyxl.Workbook()  # 新建工作蒲
    sheet = workbook.create_sheet('name')  # 新增sheet表
    data = Excel.objects.all().values('id', 'name', 'age')
    print(type(data), data)
    row_list = []
    n = 0
    for row_dic in data:  # {'name': '邓平', 'age': '8'}{'name': '云云', 'age': '5'}
        lis = []
        for i in row_dic.values():
            lis.append(i)
        row_list.append(lis)
    print(row_list)  # [['邓平', '8'], ['云云', '5']]

    for index, row_lis in enumerate(row_list):
        for index_row, row in enumerate(row_lis):
            sheet.cell(index+2, index_row+1).value = row  # cell下标1开始
            sheet.append()
    workbook.save(filename)  # 保存

    return HttpResponse('success')


def download(request):
    print(HttpResponse())
    file = 'E:/python_project/logistics/日志.txt'
    name = '日志.txt'
    f = open(file, 'rb')
    response = FileResponse(f)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(name).\
        encode('utf-8')
    print(response['Content-Disposition'])
    return response
