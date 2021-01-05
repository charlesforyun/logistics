from django.conf.urls import url
from transport import views

app_name = 'transport'

urlpatterns = [
    url(r'^apply/create/$', views.transport_apply_create, name='apply_creator'),
    url(r'^apply/delete/$', views.transport_apply_delete, name='apply_delete'),
    url(r'^apply/update/$', views.transport_apply_update, name='apply_update'),
    url(r'^apply/submit/$', views.transport_apply_submit, name='apply_submit'),
    url(r'^apply/approve/$', views.transport_apply_approve, name='apply_approve'),


]