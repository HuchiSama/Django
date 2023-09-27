from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from movie.models import *
from user import views as UserModel

movieList = ['美国往事', '小森林', '叶问', '罗马假日']


# Create your views here.
# 多对多关系
def addCollect(requset):
    for i in range(1, 10):
        Collect.objects.get_or_create(username=f'张三{i}', age=i)
    return HttpResponse('添加成功')


def addMovie(requset):
    for item in movieList:
        Movie.objects.get_or_create(name=item)

    return HttpResponse('电影添加成功')


def collectMovie(request):
    user = Collect.objects.get(username='张三1')
    movie = Movie.objects.get(name='罗马假日')

    # 添加收藏
    # 1.
    # user.movies.add(movie)
    # 2.
    movie.collect_set.add(user)
    return HttpResponse('收藏成功')


def deleteCollect(request):
    # 删除Collect
    # Collect.objects.filter(id=9).delete()
    # 删除Movie
    # Collect.objects.filter(id=1).delete()
    user = Collect.objects.get(username='张三1')
    user.movies.filter(name='叶问').delete()

    return HttpResponse('删除成功')


def query(request):
    # 获取收藏的电影
    user = Collect.objects.get(id=1)
    print(user.movies.all())
    # 获取被哪些用户收藏
    movie = Movie.objects.get(id=4)
    print(movie.collect_set.all())

    return HttpResponse('查询成功')


def getOne(request):
    print(WSGIRequest.GET())
    # for i in obj:
    #     print(i)
    # 查找某用户身份证
    user = Person.objects.get(id=2)
    print(user.idcard.idNum)
    # 查找身份对应用户
    idcard = IdCard.objects.get(id=1)
    print(idcard.person.name)
    print(request)
    return HttpResponse('查询成功')

def myRequest(request):
    # request对象的属性和方式
    # request.GET GET参数
    # request.POST POST参数
    # request.path 路径
    # print(request.GET['name']) name不存在即报错
    print(request.GET.get('name')) #不会报错，若没有返回默认值或None
    print(request.GET.getlist('name')) #若name有多个值则都会获取
    print(request.POST)
    print(request.path)
    print(request.get_full_path())

    print(request.COOKIES)
    print(request.session)

    print(request.FILE) #上传文件用
    print(request.META['REMOTE_ADDR']) #客户端IP地址
    pass
    return HttpResponse('ok')


def myResponse(request):
    pass
    #  redirect('/') 重定向
    #  HttpResponseRedirect('/') 重定向

    # 4.返回JSON
    result = {'foo': "hello", 'bar': 123, 'status_code': 200 }
    response = JsonResponse(result, status=200)
    return response