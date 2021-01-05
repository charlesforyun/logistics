from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.book),
    path('detail/list/', views.book),
    # 传递参数url
    path('need/<cate:book_id>/<cate:book_id2>/', views.need),
    # re_path("?P<book_id>")
    # /? Get 请求访问id=1
    path('need/conference/', views.conference),
    path('look/', views.books),
    path('look/<int:page>/', views.books),
    path('douban/', views.douban),
    path('read/', views.read, name='read'),
    path('movie/<dog>', views.movie, name='movie'),
    path('city/', views.city, name='city'),
    path('autospace/', views.auto_space, name='autospace'),
    path('include/', views.include)
]
# + static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS[0])

