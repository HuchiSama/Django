import math
from django.db.models import Max, Min, Sum
from django.http import HttpResponse
from django.shortcuts import render
from myApp.models import *
# Create your views here.
def demo(request):
    # return HttpResponse('hello Django!')
    return render(request, 'index.html')

def index(request):
    return HttpResponse('index')

def getUsers(request):
    users = PepleModel.objects.all()
    return render(request, 'users.html', {'users': users })


userTypes = ['青铜', '白银', '黄金', '王者']

#增加数据
def addInfo(request):
    # try:
    try:
        # record = InfoModel()
        # record.name = 'lisi'
        # record.age = 12
        # record.save()
        #-----------------
        # record = InfoModel(name='chenqi', age='27')
        # record.save()

        # ----------
        # InfoModel.objects.create(name="liba", age=18)
        # _____________

        for i in range(20):
            InfoModel.objects.get_or_create(name=f'chen{i}', age=i, type_id= i % 4 + 1)

        # ret = InfoModel.objects.get_or_create(name='wangwu', age=22)
        # print(ret)
    except Exception as e:
        print(e)
        return HttpResponse('add_fail')
    return HttpResponse('add_ok')

def addPeple(request):
    try:
        for i in range(20):
            # PepleModel.objects.get_or_create(name=f'chen{i}', age=i, type_id= i % 4 + 1)
            PepleModel.objects.get_or_create(
                name=f'li{i}',
                age=i,
                type= UserType.objects.get(pk= i% 4 + 1))

        # ret = InfoModel.objects.get_or_create(name='wangwu', age=22)
        # print(ret)
    except Exception as e:
        print(e)
        return HttpResponse('add_fail')
    return HttpResponse('add_ok')

def addUserType(request):
    for item in userTypes:
        UserType.objects.get_or_create(type=item)
    return HttpResponse('类型添加成功')
def deleteInfo(request, uid):
    try:
        #删除第一条
        res = InfoModel.objects.first(uid=uid)
        res.delete()

        #删除多条
        # InfoModel.objects.filter(name='liba').delete() #删除age大于20
    except Exception as e:
        print(e)
        return HttpResponse('delete_fail')
    return HttpResponse('delete_success!')

def deletePeple(request, uid):
    try:
        #删除第一条
        res = PepleModel.objects.all(uid=uid)
        res.delete()

        #删除多条
        # InfoModel.objects.filter(name='liba').delete() #删除age大于20
    except Exception as e:
        print(e)
        return HttpResponse('delete_fail')
    return HttpResponse('delete_success!')

def deleteUserType(request):
    try:
        #删除第一条
        res = UserType.objects.filter(id=4)
        res.delete()

        #删除多条
        # InfoModel.objects.filter(name='liba').delete() #删除age大于20
    except Exception as e:
        print(e)
        return HttpResponse('delete_fail')
    return HttpResponse('delete_success!')



def updateInfo(request):
    try:
        #第一条
        # res = InfoModel.objects.first()
        # res.age = 100
        # res.save(update_fileds=['age'])
        #----------
        InfoModel.objects.all().update(age=99)
    except Exception as e:
        print(e)
        return HttpResponse('update_fail')
    return HttpResponse('update_success!')

def getInfo(request):
    #first 获取第一条
    #last 获取最后一条
    # count 获取对象个数
    # exists 判断是否有数据，返回true || false
    # all 获取全部数据
    # values 获取指定列的值，可传多个参数，返回包含字典的列表（保存了字段名和对应值）
    # values_list 获取指定咧，可传多个参数，返回包含元祖列表（只保存值）
    try:
        # res = InfoModel.objects.get(uid=9) #pk=*** 主键=***
        # res = InfoModel.objects.filter(age__in=[99, 20]).values().values('name', 'age')
        # res = InfoModel.objects.filter(age__in=[99, 20]).filter(name='foo')

        #聚合函数， Max，Min， Sum
        # res = PepleModel.objects.aggregate(Sum('age'))
        # print(list(res), 'res', len(list(res)))

        #正向查询
        # res = PepleModel.objects.get(uid=21)
        # print(res.name, res.age, res.type_id, res.type, 'res')
        # print(res.type.type, 'type')
        # 反向查询
        #-1--------
        res = UserType.objects.get(pk = 3)
        print(res.type, res.id, 'usertype')
        # print(res.peplemodel_set.all()) #设置related_name后，当使用设置related_name的值
        print(res.peoples.all()) #设置related_name后，当使用设置related_name的值
        #-2-------
        # res = PepleModel.objects.filter(type_id=3)
        # res = PepleModel.objects.filter(type__type='黄金')
        # res = PepleModel.objects.filter(type=UserType.objects.get(pk = 3))
        # print(res, 'pepleList')

        # related_name: 关联名称

    except Exception as e:
        print(e)
        return HttpResponse('get_fail!')
    return HttpResponse(res)

def pagination(request, page = 1):
    pageSize = 10
    #page = n                  切片 [(n - 1) * pageSize : n * pageSize]
    res = InfoModel.objects.all()
    result = res[(page - 1) * pageSize : pageSize * page ]
    total = InfoModel.objects.count()
    pageCount = math.ceil(total / pageSize)

    print(result, len(result), total, pageCount)
    return HttpResponse(result)

from django.core.paginator import Paginator
# 自动分页, 分页器
def pagination2(request, page=1):
    pageSize = 15
    res = InfoModel.objects.all()
    paginator = Paginator(res, pageSize)
    currentPage = paginator.page(page) #获取第几页数据
    pageCount = paginator.page_range #页码范围
    maxPage = paginator.num_pages # 最大页数
    count = paginator.count

    print(currentPage, pageCount, maxPage, count, 'pagination2')
    return HttpResponse({
        "pageSize": pageSize,
        "list": res,
        "currentPage": currentPage,
        "pageCount": pageCount
    })
