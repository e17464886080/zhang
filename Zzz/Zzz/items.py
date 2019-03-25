# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    title = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
