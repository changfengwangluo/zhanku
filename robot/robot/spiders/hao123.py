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
    start_urls = ['http://www.163.com']

    def parse(self, response):


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
        #3，截屏[不要了，太慢了]
        #第一步，取到网页的大小。[弃用了，截图整个网页会造成图片过大，1kw张图片会达到5个t，硬盘也很贵阿。]
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.get(response.url)
        # html=driver.find_element_by_tag_name('html')
        # html_size=html.size
        #driver.close()
        #第二步，截图，需要重新实例化一个浏览器对象。
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--window-size=%d,%d' % (1920,1080))#固定大小，只截图首屏。
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.set_page_load_timeout(5)
        # driver.get(response.url,)
        # #不必等待网页全部加载完成，不然很多网站会卡住
        #
        # #拼接/判断/创建文件目录
        # dir=settings.MEDIA_ROOT+settings.MEDIA_URL+time.strftime('%Y/%m/%d')
        # if not os.path.exists(dir):
        #     os.makedirs(dir)
        # path=os.path.join(dir,hashlib.md5(str(time.time()+random.randint(0,99999)).encode('utf-8')).hexdigest()+'.jpg')
        #
        # driver.save_screenshot(path)
        #
        # image = cv2.imread(path)
        # cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 10])
        #
        # driver.close()
        # item['image'] = ''
        yield item
