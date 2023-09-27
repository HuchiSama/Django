from random import random
from django.db import models

# Create your models here.

class UserType(models.Model):
    type = models.CharField(max_length=10, unique=True)
class InfoModel(models.Model):
    desc = models.TextField(max_length=200)
    uid = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True, db_index=True)
    age = models.IntegerField(default=18)
    class Meta:
        db_table = "info_table"

    def __str__(self):
        return f'{self.uid} - {self.name} - {self.age} - {self.age}'
class PepleModel(models.Model):
    uid = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True, db_index=True)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    createTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)

    # on_delete可选值
    # models.CASCADE 表示级联删除，删除UserType是，关联的Peple也会被删除
    # models.PROTECT 保护模式，阻止级联删除
    # models.SET_NULL 置空模式，设为null， null=True参数必须具备
    # models.SET_DEFAULT 置默认值 设为默认只，default为必须参数
    # models.SET() 删除时重新动态指向一个实体访问对应元素，可传函数
    # models.DO_NOTHING 什么也不做
    # 注意: 修改on_delete参数之后需要重新同步数据

    # type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    #---------------
    # related_name: 关联名称，设置反向查找的名称，原本使用peplemodel_set改为 related_name的值
    type = models.ForeignKey(
        UserType,
        on_delete=models.PROTECT,
        related_name='peoples' # 建议使用
    )


    file = models.FileField(null=True, upload_to='static/uploads')
    # image = models.ImageField(null=True, upload_to='static/uploads')

    def __str__(self):
        return f'{self.name} - {self.age}'
