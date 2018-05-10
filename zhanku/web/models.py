from django.db import models

# Create your models here.


class WebInfo(models.Model):
    name=models.CharField(verbose_name='网站名',max_length=255,default='')
    domain_name=models.CharField(verbose_name='网站域名',max_length=255,default='',unique=True)
    image=models.ImageField(verbose_name='截图',upload_to='media/%Y/%m/%d',default='')
    pinfen=models.FloatField(verbose_name='评分',default=0)
    jianjie=models.TextField(verbose_name='简介',default='')
    dianji=models.IntegerField(verbose_name='点击',default=0)
    class Meta:
        verbose_name='网站信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
