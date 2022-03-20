from django.shortcuts import render
from django.http import HttpRequest
from start_page.check import login_check

# Create your views here.

# 云笔记首页 
# 来源：/cloudnote 前端路由的根路径
@login_check
def index(request:HttpRequest):
    if request.method == "GET":
        return render(request, 'cloudnote.html')
