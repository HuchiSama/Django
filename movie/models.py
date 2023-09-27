from django.db import models

# Create your models here.
# 用户：电影 多对多关系 N ：M
# 一个用户收藏多部电影，一个电影被多个用户收藏
# 电影:
class Movie(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField(default=90)
    class Meta:
        pass
    def __str__(self):
        return f'{self.name}-{self.duration}'
class Collect(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    # 多对多关系
    movies = models.ManyToManyField(Movie)
    def __str__(self):
        return f'{self.username}'

class IdCard(models.Model):
    idNum = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.idNum)

class Person(models.Model):
    idcard = models.OneToOneField(IdCard, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name