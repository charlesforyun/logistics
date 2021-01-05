from django.urls import path
from apps.index import views

app_name = 'index'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
    # path('transfer/', views.TransferView.as_view(), name='transfer'),
]