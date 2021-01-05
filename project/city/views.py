from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.shortcuts import render
from datetime import datetime
from django.db import connection


class Game():
    def __init__(self, name):
        self.name = name


book_list = [
    "水浒传",
    "西游记",
    "红楼梦",
    "三国演义"
]


def book(request):
    p = Game('lol')
    context = {
        'username': {
            'zhiliao': 'dengping'
        },
        'game': p,
        'age': 18,
        'books': [
            '红楼梦',
            '西游记',
            '水浒传',
            '三国演义'
        ],
        'person': {
            'username': 'dengping',
            'age': 18,
            'height': 180
        },
        'booklove': [
            {
                '书名': '三国演义',
                '作者': '罗贯中',
                '价格': 20
            },
            {
                '书名': '水浒传',
                '作者': '施耐庵',
                '价格': 25
            },
            {
                '书名': '红楼梦',
                '作者': '曹雪芹',
                '价格': 99
            },
            {
                '书名': '西游记',
                '作者': '罗贯中',
                '价格': 89
            }
        ]
    }
    # list = render_to_string('book.html')
    return render(request, 'book.html', context=context)


def books(request, page=0):
    return HttpResponse(book_list[page])


def need(request, book_id, book_id2):
    text = "您获取的图书：%s%s" % (book_id, book_id2)
    return HttpResponse(text)


def conference(request):
    """视图函数传递url键值对"""
    conference_id = request.GET.get('id')
    text = 'conference:%s' % conference_id
    return HttpResponse(text)


def douban(request):
    return render(request, 'url.html')


def read(request):
    read = request.GET.get('name')
    return HttpResponse(read)


def movie(request, dog):
    return HttpResponse('电影首页')


def city(request):
    return render(request, 'include.html')


def auto_space(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(id,name,author) values(null,'三国演义','罗贯中')")
    cursor.execute("select id,name,author from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    context = {
        'info': "<a href='www.baidu.com'>百度</a>",
        'birthday': datetime.now(),
        'file': 'name:',
        'datatime': datetime(year=2018, month=11, day=19,
                             hour=21, minute=8, second=0)
    }
    return render(request, 'autoescape.html', context=context)


def include(request):
    return render(request, 'include.html')
