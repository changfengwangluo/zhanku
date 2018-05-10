# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from web.models import WebInfo

class RobotPipeline(object):
    def process_item(self, item, spider):
        domain_name=item['domain_name']
        result=WebInfo.objects.filter(domain_name=domain_name).first()
        if result is None:
            WebInfo.objects.create(domain_name=item['domain_name'],title=item['title'],keywords=item['keywords'],desc= item['desc'])
        return item
