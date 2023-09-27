import hashlib
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from user.models import *

# Create your views here.

def login(request):
    name = request.GET.get('name')
    pwd = request.GET.get('pwd')
    md5 = hashlib.md5()

    md5.update(pwd.encode())
    resPwd = md5.hexdigest()
    print(request.GET, 'get', name, resPwd)

    userItem = UserModel.objects.filter(name=name, pwd=resPwd)
    print(userItem)
    if (userItem.exists()):
        response = JsonResponse({'message': 'login success'})
        uidMD5 = hashlib.md5()
        uidMD5.update(str(userItem[0].id).encode())
        print(uidMD5.hexdigest())
        # cookie校验
        # response.set_cookie('uid',uidMD5.hexdigest(), max_age=7*24*3600)
        # response.set_cookie('uid', userItem[0].id, expires=datetime.datetime.now() + datetime.timedelta(days=7))
        # response.delete_cookie()
        # session校验
        request.session['uid'] = userItem[0].id
        request.session.set_expiry(86400*7) #过期时间
        return response
    # MD5.ADD()
    print(request.COOKIES, 'login')
    return JsonResponse({'message': 'login fail'})

def register(request):
    name = request.GET.get('name')
    pwd = request.GET.get('pwd')
    md5 = hashlib.md5()

    md5.update(pwd.encode())
    resPwd = md5.hexdigest()
    print(request.GET, 'get', name, resPwd)

    if (name and pwd):
        UserModel.objects.get_or_create(name=name, pwd = resPwd)
        return JsonResponse({'message': 'success'})

    return JsonResponse({'message': 'fail'})

def logout(request):
    # cookie
    # uid = request.COOKIES.get('uid')
    # if (not uid):
    #     return JsonResponse({'message': 'please login'})
    # response = JsonResponse({'message': 'logout success'})
    # response.delete_cookie('uid')
    #session
    response = HttpResponseRedirect('/login')
    session_key = request.session.session_key
    if (not session_key):
        return JsonResponse({'message': 'please login'})
    print(session_key, 'session_key')
    request.session.delete(session_key)
    #跳转刷新页面session_key才会被浏览器删除

    return response
