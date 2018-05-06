# -*- coding: utf-8 -*-
import scrapy
from web.models import WebInfo
from robot.items import RobotItem
import tldextract


class AizhanSpider(scrapy.Spider):
    name = 'alexa'
    # allowed_domains = ['https://www.aizhan.com/']
    start_urls = ['http://www.alexa.cn/baidu.com/']

    def parse(self, response):
        #http://www.alexa.cn/kmpmdp.cn
        urls = response.xpath('//a/@href').re('www.alexa.cn\/(.*)')
        for url in urls:

            ext = tldextract.extract(url=url)
            domain_name = ext.registered_domain
            if domain_name != '':
                item = RobotItem()
                item['name'] = ''
                item['domain_name'] = 'http://' + domain_name

                yield item
                yield scrapy.Request(url='http://www.alexa.cn/' + domain_name, callback=self.parse)


    custom_settings = {
        'CONCURRENT_REQUESTS' : 1,
        'RANDOMIZE_DOWNLOAD_DELAY' : False,
        'DOWNLOAD_DELAY' : 60 / 60.0,
        'CONCURRENT_REQUESTS_PER_IP' : 40,
    }
