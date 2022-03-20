# 后端路由
# 关于不走二级app的问题
# 前端路由生成的都是一级的地址
# 例如 /login  /resgiter 无法转到二级路由

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from start_page.check import login_check

# 用户登出
# 来源 /logout
def logout(request:HttpRequest):
    if request.method == "GET":
        resp = HttpResponseRedirect('/')
        resp.delete_cookie('username')
        resp.delete_cookie('uid')
        resp.delete_cookie('sessionid')
        return resp

# 用户登录
# 来源 /login
def login(request: HttpRequest):
    if request.method == "GET":
        if request.session.get('uid'):
            username = request.session['username']
        elif request.COOKIES.get('uid'):
            username = request.COOKIES['username']
        else:
            # 没有登录返回登陆页面
            return render(request, 'login.html')
        # 已经登陆 重定向首页
        return HttpResponseRedirect('/')

# 个人空间
# 来源：/space
@login_check
def space(request:HttpRequest):
    if request.method == "GET":
        return render(request, 'space.html')