# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from web.models import WebInfo, Keywords
import re
from twisted.enterprise import adbapi
from . import settings
import pymysql
import asyncio

class RobotPipeline(object):
    def process_item(self, item, spider):
        # WebInfo.objects.create(domain_name=item['domain_name'], title=item['title'], keywords=item['keywords'],
        # desc=item['desc'])
        return item

class AsyncioPipeline(object):



    def process_item(self, item, spider):
        # 执行coroutine
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.do_insert(item=item))
        ollp.close()
        return item

    def do_insert(self,item):
        WebInfo.objects.create(domain_name=item['domain_name'], title=item['title'], keywords=item['keywords'],
                               desc=item['desc'])


# 异步插入数据
# Twisted只是提供一个异步容器，本身没提供数据库链接
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 从配置中获取信息
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入编程异步执行
        # 第一个参数是我们定义的函数
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 错误处理
    #     query.addErrorback(self.handle_error)
    #
    #     # 错误处理函数
    # def handle_error(self, falure):
    #     print(falure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        WebInfo.objects.create(domain_name=item['domain_name'], title=item['title'], keywords=item['keywords'],
        desc=item['desc'])


class KeywordsPipeline(object):

    def process_item(self, item, spider):
        keywords_arr = re.split(r',|-|_|，|\|.|。|、', item['keywords'])
        for keyword in keywords_arr:
            Keywords.objects.create(keyword=keyword)

        return item
