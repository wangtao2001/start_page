from django.http import HttpResponseRedirect, HttpRequest


# 装饰器，检查有没有登录，如果没有
# 对于一些需要登录才能查看的页面，需要先跳转到登录
# next 表示登陆后跳转到哪，即跳转到原来访问的页面
def login_check(func):
    def wrap(request: HttpRequest, *args, **kwargs):
        if not request.session.get('username') or not request.session.get('uid'):
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_uid or c_username:
                return HttpResponseRedirect(f'/login?next={request.path_info}')
            else:
                request.session['username'] = c_username
                request.session['c_uid'] = c_uid
        return func(request, *args, **kwargs)

    return wrap
