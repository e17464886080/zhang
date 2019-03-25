# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,pymysql
from  .settings import *
class ZzzPipeline(object):
    def process_item(self, item, spider):
        #会将item交给下一个管道使用
        return item

class TengxunPipelines():
    def open_spider(self,spider):
        print('spider')
        # self.coon=pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        # self.db=self.coon[MONGO_DB]
        # self.myset=self.db[MONGO_SET_]

    def process_item(self, item, spider):
        # 会将item交给下一个管道使用
        # self.myset.insert_one(dict(item))
        return item
    def close_spider(self,spider):
        # self.coon.close()
        print('close')
