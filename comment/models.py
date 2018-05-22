from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    ###关联评论的对象，利用contenttypes。
    content_type=models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)#ContentType指向任何类型
    object_id=models.PositiveIntegerField()#指向类型对象的id
    content_object=GenericForeignKey('content_type','object_id')#注册他们
    ###
    text=models.TextField(verbose_name='评论内容',default='')
    conment_time=models.DateField(verbose_name='评论时间',default= datetime.now)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.text

