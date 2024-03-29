"""lynnwangsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views import static
from django.conf import settings
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('summernote/', include('django_summernote.urls')),
    path('', index),
    path('blogs', blogs),
    re_path(r'^blogs/(?P<page>\d+)$', blogs),
    re_path(r'^post/(?P<id>\d+)$', post),
    re_path(r'^post/(?P<name>[-\w]+)$', post_name),
    path('projects', projects),
    re_path(r'^projects/(?P<page>\d+)$', projects),
    re_path(r'^tags/(?P<tag>\w+)$', tags),
    re_path(r'^tags/(?P<tag>\w+)/(?P<page>\d+)$', tags),
    path('about', about),
    path('resume', resume),
]
