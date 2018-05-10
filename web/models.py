from django.db import models
from datetime import datetime
# Create your models here.


class WebInfo(models.Model):

    domain_name=models.CharField(verbose_name='网站域名',max_length=255,default='',unique=True)
    domain_reg_time = models.DateTimeField(verbose_name='域名注册时间', default=datetime.today)
    domain_reg_person=models.CharField(verbose_name='域名注册人',max_length=255,default='')

    title = models.CharField(verbose_name='网站标题', max_length=255, default='')
    keywords = models.TextField(verbose_name='网站关键词', max_length=255, default='')
    desc = models.TextField(verbose_name='网站描述', max_length=255, default='')
    jianjie = models.TextField(verbose_name='网站简介', max_length=255, default='')

    beian=models.CharField(verbose_name='备案号',max_length=255,default='')
    beian_name=models.CharField(verbose_name='备案名称',max_length=255,default='')
    beian_cate=models.CharField(verbose_name='备案性质',max_length=255,default='')
    domain_time = models.DateTimeField(verbose_name='备案审核时间', default=datetime.today)

    qq=models.CharField(verbose_name='联系QQ',max_length=255,default='')
    weixin=models.CharField(verbose_name='联系微信',max_length=255,default='')
    tel=models.CharField(verbose_name='联系电话',max_length=255,default='')
    phone=models.CharField(verbose_name='联系手机',max_length=255,default='')

    ip=models.CharField(verbose_name='联系QQ',max_length=255,default='')

    class Meta:
        verbose_name='网站信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
