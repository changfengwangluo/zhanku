from django.db import models

# Create your models here.


class WebInfo(models.Model):
    name=models.CharField(verbose_name='网站名',max_length=255,default='')
    domain_name=models.CharField(verbose_name='网站域名',max_length=255,default='',unique=True)

    class Meta:
        verbose_name='网站信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
