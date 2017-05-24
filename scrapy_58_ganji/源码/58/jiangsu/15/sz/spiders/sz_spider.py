# -*- coding: utf-8 -*-
__author__ = 'Windows'

import scrapy
from scrapy.http import Request
from sz.items import SzItem

class sz_spider(scrapy.Spider):
    name = "jiangsu"
    allowed_domains=['58.com',]

    city = "rugao"
    #在网址处更改城市名称
    start_urls=[
                'http://{0}.58.com/danbaobaoxiantouzi/pn1/'.format(city),
                ]

    def parse(self,response):
        link = response.xpath('//a[@class="t"]/@href').extract()
        for link_url in link:
            yield Request(link_url,callback=self.parse_shop)

        next_link = response.xpath('//a[@class="next"]/@href').extract()
        if next_link:
            next_page = 'http://{0}.58.com'.format(self.city)+next_link[0]
            print u"下一页是："+next_page
            yield Request(next_page,callback=self.parse)


    def parse_shop(self,response):
        shop = response.xpath('//div[@class="userinfo-link"]/a/@href').extract()
        yield Request(shop[0],callback=self.parse_item)


    def parse_item(self,response):
        item = SzItem()
        item['name']=response.xpath('//div[@id="fendian_0"]/h3/text()').extract()[0]
        item['address']=response.xpath('//div[@id="fendian_0"]/p/text()').extract()[0]
        item['tel']=response.xpath('//div[@id="fendian_0"]/p[@class="telNoBox"]/b/text()').extract()[0]
        yield item