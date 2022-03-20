from tokenize import group
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . import models
import hashlib
from django.db.utils import IntegrityError
import requests
import re

# 暂时JSON数据只能从前端以字符串形式传递
# 此函数将传递值解析为dict
def parser(post):
    print(post)
    return eval(list(dict(post).keys())[0])


# api测试
# 来源 /api/
@csrf_exempt
def api(request: HttpRequest):
    if request.method == 'GET':
        resp = {'code': 200,'data':{}, 'messgae': 'get api data success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    elif request.method == 'POST':
        resp = {"code": 200, 'data':{}, 'messgae': 'post api data success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

# 登录功能
# 来源 /api/login/
@csrf_exempt
def login(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponseRedirect("/login/")
    elif request.method == 'POST':
        data = parser(request.POST)
        if data['mode'] != 'login':
            # 请求格式错误
            resp = {'code': 100,'data': {},'message':'请求格式错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        # 登录过程
        username = data['data']['username']
        password = data['data']['password']
        remember = data['data']['remember'] # 是否记住登录
        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist as e:
            # 不存在用户
            resp = {'code': 201,'data': {},'message':'用户名不存在'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            # 账号或密码错误
            resp = {'code': 202,'data': {'next': request},'message':'账号户密码错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        request.session['username'] = username
        request.session['uid'] = user.id
        
        # 登陆成功
        resp = {'code': 200,'data': {},'message':'登陆成功'}
        r = HttpResponse(json.dumps(resp), content_type="application/json")
        # 记住登录15天
        if remember == "true":
            r.set_cookie('username', username, 3600*24*15)
            r.set_cookie('uid', user.id, 3600*24*15)
        return r

# 关于用户注册功能
# 如果绕过前端，这里也是可以检测的（用户名密码非空，用户名密码格式）
# 注册功能
# 来源 /api/register/
@csrf_exempt
def register(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponseRedirect("/login/")
    elif request.method == 'POST':
        data = parser(request.POST)
        if data['mode'] != 'register':
            # 请求格式错误
            resp = {'code': 100,'data': {},'message':'请求格式错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        # 执行注册过程
        username = data['data']['username']
        password = data['data']['password']
        # 这里后端并不需要验证重复密码
        if username == "":
            # 用户名为空
            resp = {'code': 300,'data': {},'message':'用户名为空'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        username_reg = r"^[a-zA-Z0-9_]{2,10}$"
        if not (re.match(username_reg, username).group(0) == username):
            # 用户名不符合 ‘2-10位字母、数字、下划线’
            resp = {'code': 300,'data': {},'message':'用户名格式错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        if models.User.objects.filter(username=username):
            # 用户已经存在
            resp = {'code': 101,'data': {},'message':'用户名已存在'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        pwd_reg = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{2,10}$'
        if not (re.match(pwd_reg, password).group(0) == password):
            # 密码不符合 ‘必须包含大小写字母、数字、不能使用特殊字符’
            resp = {'code': 300,'data': {},'message':'密码格式错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
    
        # 密码加密
        m = hashlib.md5()
        m.update(password.encode())
        password = m.hexdigest()
        try:
            user = models.User.objects.create(username=username, password=password)
        except IntegrityError as e:
            # 用户已经存在
            resp = {'code': 101,'data': {},'message':'用户名已存在'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        # 注册成功
        # 重定向到登录页
        resp = {'code': 200,'data': {},'message':'注册成功'}
        return HttpResponse(json.dumps(resp), content_type="application/json") 


# 获取用户信息 例如已经登录的用户名，头像等等
# 例如 个人空间 显示 欢迎：某某某，只能从这里得到信息
# 因为是前后端分离的，所以不可能返回模板同时返回信息
# 需要强制登录的页面，在这里不会出现未登录的情况的，必然能获取到信息
# 非强制登录的页面，可能会有，例如首页
# 来源/api/userInfo
@csrf_exempt
def userInfo(request:HttpRequest):
    if request.method == 'POST':
        data = parser(request.POST)
        if data['mode'] != 'userInfo':
            # 请求格式错误
            resp = {'code': 100,'data': {},'message':'请求格式错误'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        # 执行登录检查过程
        if request.session.get('uid'):
            username = request.session['username']
        elif request.COOKIES.get('uid'):
            username = request.COOKIES['username']
        else:
            # 用户未登录
            resp = {'code': 203,'data': {},'message':'用户未登录'}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        # 查询信息
        # 因为这里暂时只涉及到查询用户名
        query = data['data']
        # 所以不循环数组了，直接返回
        resp = {'code': 200,'data': {'username': username},'message':'用户未登录'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

# 获取搜索建议
# 来源/api/suggestion
@csrf_exempt
def suggestion(request:HttpRequest):
    if request.method == 'GET':
        content = request.GET.get('wd')
        url = f"http://suggestion.baidu.com/su?wd={content}&p=3"
        r = requests.get(url)
        li = eval(re.search('\[.*\]',r.text.lstrip('window.baidu.sug(').rstrip(');')).group(0))
        resp = {'code': 200,'data': li[:9],'message':'获取成功'}
        return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json")

# bing每日一图
# 来源/api/bing
def bing(request:HttpRequest):
    if request.method == 'GET':
        api = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1" # idx=0表示今日数据
        r = requests.get(url=api)
        data = json.loads(r.text)
        url = 'https://cn.bing.com' + data['images'][0]['url']
        info = data['images'][0]['copyright']
        mode = request.GET["mode"]
        if mode == 'bg': # 每日一图资源
            return HttpResponseRedirect(url)
        elif mode == 'info': # 每日一图介绍
            resp = {'code': 200,'data': info,'message':'获取成功'}
            return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json")

        
