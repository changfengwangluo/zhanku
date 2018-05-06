# -*- coding: utf-8 -*-
import scrapy
from web.models import WebInfo
from robot.items import RobotItem
import tldextract


class AizhanSpider(scrapy.Spider):
    name = 'aizhan'
    # allowed_domains = ['https://www.aizhan.com/']
    start_urls = ['https://www.aizhan.com/cha/www.baidu.com/']

    def parse(self, response):
        # 'https://www.aizhan.com/cha/m.27bao.com/' 地址都是这样子的，需要正则匹配以下。
        urls = response.xpath('//a/text()').extract()
        for url in urls:

            ext = tldextract.extract(url=url)
            domain_name = ext.registered_domain
            if domain_name != '':
                item = RobotItem()
                item['name'] = ''
                item['domain_name'] = 'http://' + domain_name

                yield item
                yield scrapy.Request(url='https://www.aizhan.com/cha/' + domain_name, callback=self.parse)



    custom_settings = {
        'CONCURRENT_REQUESTS' : 1,
        'RANDOMIZE_DOWNLOAD_DELAY' : False,
        'DOWNLOAD_DELAY' : 60 / 60.0,
        'CONCURRENT_REQUESTS_PER_IP' : 40,
    }
