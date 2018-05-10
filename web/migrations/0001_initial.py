# Generated by Django 2.0.2 on 2018-05-10 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(default='', max_length=255, unique=True, verbose_name='网站域名')),
                ('domain_reg_time', models.DateTimeField(default=datetime.datetime.today, verbose_name='域名注册时间')),
                ('domain_reg_person', models.CharField(default='', max_length=255, verbose_name='域名注册人')),
                ('title', models.CharField(default='', max_length=255, verbose_name='网站标题')),
                ('keywords', models.TextField(default='', max_length=255, verbose_name='网站关键词')),
                ('desc', models.TextField(default='', max_length=255, verbose_name='网站描述')),
                ('jianjie', models.TextField(default='', max_length=255, verbose_name='网站简介')),
                ('beian', models.CharField(default='', max_length=255, verbose_name='备案号')),
                ('beian_name', models.CharField(default='', max_length=255, verbose_name='备案名称')),
                ('beian_cate', models.CharField(default='', max_length=255, verbose_name='备案性质')),
                ('domain_time', models.DateTimeField(default=datetime.datetime.today, verbose_name='备案审核时间')),
                ('qq', models.CharField(default='', max_length=255, verbose_name='联系QQ')),
                ('weixin', models.CharField(default='', max_length=255, verbose_name='联系微信')),
                ('tel', models.CharField(default='', max_length=255, verbose_name='联系电话')),
                ('phone', models.CharField(default='', max_length=255, verbose_name='联系手机')),
                ('ip', models.CharField(default='', max_length=255, verbose_name='联系QQ')),
            ],
            options={
                'verbose_name': '网站信息',
                'verbose_name_plural': '网站信息',
            },
        ),
    ]
