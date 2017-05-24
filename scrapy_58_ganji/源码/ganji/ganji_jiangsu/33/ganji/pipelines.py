# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings

class GanjiPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings[ 'MONGODB_SERVER' ],
            settings[ 'MONGODB_PORT' ]
        )
        db = connection[settings[ 'MONGODB_DB' ]]
        self.collection = db[settings[ 'MONGODB_COLLECTION' ]]

    def process_item(self, item, spider):

        name = item['name']
        address=item['address']
        tel=item['tel']

        print u"公司名称："+name
        print u"公司地址："+address
        print u"联系电话："+tel
        print "------------------------------------------------------------------"
        print "------------------------------------------------------------------"

        self.collection.insert(dict(item))

        return item

