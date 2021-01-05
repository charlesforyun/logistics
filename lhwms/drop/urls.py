from django.conf.urls import url
from drop import views

app_name = 'drop'

urlpatterns = [
    url(r'^apply/create/$', views.drop_apply_create, name='apply_creator'),
    url(r'^apply/delete/$', views.drop_apply_delete, name='apply_delete'),
    url(r'^apply/update/$', views.drop_apply_update, name='apply_update'),
    url(r'^apply/submit/$', views.drop_apply_submit, name='apply_submit'),
    url(r'^apply/approve/$', views.drop_apply_approve, name='apply_approve'),
]