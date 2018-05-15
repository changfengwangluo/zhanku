from django.db import models
from datetime import datetime
# Create your models here.


class WebInfo(models.Model):

    domain_name=models.CharField(verbose_name='网站域名',max_length=255,default='',unique=True)
    title = models.CharField(verbose_name='网站标题', max_length=255, default='')
    keywords = models.TextField(verbose_name='网站关键词', max_length=255, default='')
    desc = models.TextField(verbose_name='网站描述', max_length=255, default='')
    create_time=models.DateField(verbose_name='收录时间',default=datetime.now)

    class Meta:
        verbose_name='网站信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class Keywords(models.Model):
    keyword=models.CharField(verbose_name='关键词',max_length=255,default='',unique=True)

    class Meta:
        verbose_name='关键词'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.keyword

class Searchs(models.Model):
    keyword=models.CharField(verbose_name='搜索词',max_length=255,default='',unique=True)

    class Meta:
        verbose_name='用户搜索'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.keyword
