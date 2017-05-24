# -*- coding:utf-8 -*-
__author__ = 'Windows'

import scrapy
from scrapy.http import Request
from ganji.items import GanjiItem
import re


class ganji_spider(scrapy.Spider):
    name = "ganji"
    allowed_domains=['ganji.com',]

    city = "shaoxing"
    #在网址处更改城市名称
    start_urls=[
                'http://{0}.ganji.com/danbaobaoxian/'.format(city),
                ]


    item = GanjiItem()
    def parse(self,response):

        img_url_list =  response.xpath('//li[@class="list-img"]/div[@class="txt"]/p[@class="t"]/a/@href').extract()
        phone_list = response.xpath('//li[@class="list-img"]/div[@class="list-r-area"]/p[@class="tel"]/a/@data-phone').extract()

        length = len(img_url_list)
        for n in range(0,length):
            self.item['tel'] = phone_list[n]
            #print self.item['tel']

            img_url = img_url_list[n]
            #print img_url
            a = re.findall(r'su(.+?)com',img_url)
            if len(a)==0:
                img_detail = "http://{0}.ganji.com".format(self.city)+img_url
            else:
                img_detail= "http:{0}".format(img_url)

            print u"有图片的链接是："+img_detail
            yield Request(img_detail,callback=self.parse_img)

        no_img_list = response.xpath('//li[@class="list-noimg"]/div[@class="txt"]/p[1]/a/@href').extract()
        for no_img_url in no_img_list:
            no_img_url = "http://{0}.ganji.com".format(self.city)+no_img_url
            print u"没有图片的链接是："+no_img_url
            yield Request(no_img_url,callback=self.parse_no_img)


        next_link = response.xpath('//a[@class="next"]/@href').extract()
        if next_link:
            next_page = 'http://{0}.ganji.com'.format(self.city)+next_link[0]
            print u"下一页是："+next_page
            yield Request(next_page,callback=self.parse)

    def parse_img(self,response):
        m = 1
        text = response.xpath('//ul[@id="tabl"]/li[{0}]/a/text()'.format(m)).extract()[0]
        #print text

        while text != u'联系方式':
            m = m+1
            text =  response.xpath('//ul[@id="tabl"]/li[{0}]/a/text()'.format(m)).extract()[0]
            #print text
        else:
            link = response.xpath('//ul[@id="tabl"]/li[{0}]/a/@href'.format(m)).extract()[0]
            link = "http://{0}.ganji.com".format(self.city)+link

        #print link
        yield Request(link,callback=self.parse_img_detail)


    def parse_img_detail(self,response):

        print u"我在解析有图片的链接啊啊啊啊~~~~"

        name = response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[2]/div[@class="fl"]/h1/text()').extract()[0]
        self.item['name'] = name

        z = 3
        title = response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/span[@class="t"]/text()'.format(z)).extract()[0]
        #print title

        while title != u'商家地址：':
            z = z+1
            title =  response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/span[@class="t"]/text()'.format(z)).extract()[0]
            #print title

        else:
            address =  response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/p[@class="fl"]/text()'.format(z)).extract()
            length = len(address)
            #print length
            y = 0
            add = ""
            while y < length:
                add = add +address[y]
                y = y+1
            else:
                self.item['address'] = add

        #print self.item['address']
        yield self.item


    def parse_no_img(self,response):

        print u'解析文字的链接来啦啦啦啦啦阿拉！！！！'

        name = response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[2]/div[@class="fl"]/h1/text()').extract()[0]
        self.item['name'] = name

        z = 3
        title = response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/span[@class="t"]/text()'.format(z)).extract()[0]
        #print title

        while title != u'商家地址：':
            z = z+1
            title =  response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/span[@class="t"]/text()'.format(z)).extract()[0]
        #    print title

        else:
            address =  response.xpath('//div[@id="dzcontactus"]/div[@class="con"]/ul/li[{0}]/p[@class="fl"]/text()'.format(z)).extract()
            length = len(address)
        #    print length
            y = 0
            add = ""
            while y < length:
                add = add +address[y]
                y = y+1
            else:
                self.item['address'] = add

        #print self.item['address']


        number = response.xpath('//div[@class="tcon pos-r"]/a/@gjalog').extract()[0]
        self.item['tel']=re.findall(r'@phone=(.+?)@',number)[0]
        #print self.item['tel']

        yield self.item


