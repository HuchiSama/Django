from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=200, unique=True)