"""chat_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve

from chat_api import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^%s/static/(?P<path>.*)$' % settings.PRO_URL, serve,
            {'document_root': settings.STATIC_ROOT}),  # 静态文件
    re_path(r'^%s/logview/(?P<path>.*)$' % settings.PRO_URL, serve,
            {'document_root': settings.LOG_DIR}),  # 日志下载
    re_path(r'^%s/apidoc/(?P<path>.*)$' % settings.PRO_URL, serve,
            {'document_root': settings.APIDOC_STATIC_SITE})  # apidoc
]
