from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    # api 数据接口测试
    url('^$', views.api),
    url('^login/', views.login),
    url('^register/', views.register),
    url('^userInfo/$', views.userInfo),
    url('^suggestion/$', views.suggestion),
    url('^bing/$', views.bing)
]