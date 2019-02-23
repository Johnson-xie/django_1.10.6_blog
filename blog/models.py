from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):

    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):

    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    article_abstract = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)  # django内置模块

# 查看具体sql语句
# python manage.py sqlmigrate blog 0001

