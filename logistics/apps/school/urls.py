from django.urls import path
from apps.school import views

app_name = 'school'

urlpatterns = [
    path('', views.EnterScore.as_view(), name='enter_score'),
    path('score/', views.ShowList.as_view(), name='show_score'),
    path('openpyxl/', views.excel_write, name='openpyxl'),
    path('download/', views.download, name='download')
]