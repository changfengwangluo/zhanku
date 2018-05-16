# -*- coding: utf-8 -*-
import scrapy
import tldextract
from robot.items import RobotItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from zhanku import settings
import time,os,re,hashlib,random,cv2



class Hao123Spider(scrapy.Spider):
    name = 'hao123'
    # allowed_domains = ['www.hao123.com']
    start_urls = ['http://www.0430.com']

    def parse(self, response):
        #result=re.findall(ur'[\u4e00-\u9fa5]',test.decode('utf-8'))
        result=re.findall('[\u4e00-\u9fa5]',response.text)#匹配到了中文，才继续工作
        if len(result)>0:
            urls = response.xpath('//a/@href').extract()
            # 每一个网址访问进来做两件事：1，抓取里面的网址，2，获取网站信息。3，对首页进行截屏。
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
            item['title'] =  response.xpath('//title/text()').extract_first()
            item['keywords']=''
            item['desc']=''
            # metas = response.xpath('//meta').extract()
            # for meta in metas:
            #     meta = meta.replace('"', '#')  # 替换双引号
            #     meta = meta.replace("'", '#')  # 替换单引号
            #     meta = meta.replace(' ', '')  # 去除所有空格
            #     meta = meta.lower()  # 转小写
            #     if meta.find('keyword') > 0 and meta.find('content') > 0:
            #         item['keywords'] = re.findall('content=#(.*?)#',meta)[0]#关键词
            #
            #     if meta.find('description') > 0 and meta.find('content') > 0:
            #         item['desc'] = re.findall('content=#(.*?)#',meta)[0]#描述
            if item['title'] is not None:
                yield item
