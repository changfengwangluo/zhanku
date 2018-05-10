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
        # 每一个网址访问进来做两件事：1，抓取里面的网址，2，获取网站信息。
        # 1，处理网址
        for url in urls:
            ext = tldextract.extract(url=url)
            domain_name = ext.registered_domain
            if domain_name != '':
                domain_name = 'http://www.' + domain_name
                yield scrapy.Request(url=domain_name, callback=self.parse)
        # 2，处理网站信息
        item = RobotItem()
        item['domain_name'] = 'http://www.' + tldextract.extract(url=response.url).registered_domain
        item['title'] = response.xpath('//title/text()').extract_first()
        metas = response.xpath('//meta').extract()
        for meta in metas:
            meta = meta.replace('"', '#')  # 替换双引号
            meta = meta.replace("'", '#')  # 替换单引号
            meta = meta.replace(' ', '')  # 去除所有空格
            meta = meta.lower()  # 转小写
            if meta.find('keyword') > 0 and meta.find('content') > 0:
                item['keywords'] = re.findall('content=#(.*?)#',meta)[0]
            if meta.find('description') > 0 and meta.find('content') > 0:
                item['desc'] = re.findall('content=#(.*?)#',meta)[0]
        yield item
