from django.urls import path, re_path
from . import views

# 应用命名空间
# 应用命名空间的变量叫做app_name
app_name = 'cms'

urlpatterns = [
    path('', views.index),
    path('sing/', views.login, name='login'),
    re_path(r"reverse/(?P<nian>[0-9]{4})/(?P<yue>[0-9]{2})", views.reverse2,
            name='reverse'),
    path('reverse/', views.reverse1, name='re'),
    # re_path(r"^PD$", views.reverse)
]
