from django.conf.urls import url
from outgoing import views

app_name = 'outgoing'

urlpatterns = [
    url(r'^apply/create/$', views.outgoing_apply_create, name='apply_creator'),
    url(r'^apply/delete/$', views.outgoing_apply_delete, name='apply_delete'),
    url(r'^apply/update/$', views.outgoing_apply_update, name='apply_update'),
    url(r'^apply/submit/$', views.outgoing_apply_submit, name='apply_submit'),
    url(r'^apply/approve/$', views.outgoing_apply_approve, name='apply_approve'),
    url(r'^apply/accessory/uploading/$', views.outgoing_accessory_uploading,
        name='apply_accessory_uploading'),
    url(r'^apply/accessory/delete/$', views.outgoing_accessory_delete,
        name='apply_accessory_delete'),
]