# -*- coding: utf-8 -*-
import scrapy
import tldextract
from robot.items import RobotItem
import re



class Hao123Spider(scrapy.Spider):
    name = 'hao123'
    # allowed_domains = ['www.hao123.com']
    start_urls = ['http://www.hao123.com/']

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            ext = tldextract.extract(url=url)
            domain_name = ext.registered_domain
            if domain_name!='':
                domain_name='http://'+domain_name
                item = RobotItem()
                item['name'] = ''
                item['domain_name'] = domain_name

                yield item
                yield scrapy.Request(url=domain_name, callback=self.parse)
