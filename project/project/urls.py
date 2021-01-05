"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('book/', include(('city.urls', 'city'), namespace='book')),
    # path('book/detail/', city.detail)
    path('', include('front.urls')),
    path('cms1/', include('cms.urls', namespace='cms1')),
    path('cms2/', include('cms.urls', namespace='cms2'))
    # path('cms', include(('city.urls', 'book'), namespace='1'))
    # path('cms', include（[path()],('city.urls', 'book', namespace='2')）
]
