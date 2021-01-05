from django.conf.urls import url, include
from django.contrib import admin
from user.views import login, index

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^login$', login.login, name='login'),
    url(r'^do_login$', login.do_login, name='do_login'),
    url(r'^logout$', login.logout, name='logout'),
    url(r'^index$', index.index, name='index'),

    url(r'^user/', include('user.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^log/', include('log.urls')),
    url(r'^incoming/', include('incoming.urls')),
    url(r'^outgoing/', include('outgoing.urls')),
    url(r'^drop/', include('drop.urls')),
    url(r'^transport/', include('transport.urls')),
    url(r'^inventory/', include('inventory.urls')),
]
