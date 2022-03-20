"""start_page URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    # 以下匹配的都是完全路径
    # 所有的数据请求都会转到后端处理
    url('^api/', include('backend.urls')),
    # 根目录 匹配完全根目录
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # 注册页面
    url('^login/$', views.login),
    # 前端路由history模式导致的重定向
    url('^register/$', lambda request: HttpResponseRedirect("/login/")),
    # 登出功能
    url('^logout/$', views.logout),
    # 个人空间，暂未做
    url('^space/$', views.space),
    # 云笔记 分布式路由
    url('^cloudnote/', include('cloudnote.urls'))
]
