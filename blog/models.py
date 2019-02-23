from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
class Category(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=50)
    body = models.TextField()
    # TODO 时间自动修改
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    article_abstract = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)  # django内置模块
    def __str__(self):
        return self.title

# 查看具体sql语句
# python manage.py sqlmigrate blog 0001

