# -*- coding: utf-8 -*-

import scrapy
from ..items import *

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/']

    def parse(self, response):

        item=TengxunItem()
        rList=response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for r in rList:
            title=r.xpath('./td[1]/a/text()').extract_first()
            type=r.xpath('./td[2]/text()').extract_first()
            num=r.xpath('./td[3]/text()').extract_first()
            address=r.xpath('./td[4]/text()').extract_first()
            time=r.xpath('./td[5]/text()').extract_first()
            link=r.xpath('./td[1]/a/@href').extract_first()
            link= response.url+link
            item['title']=title
            item['type']=type
            item['num']=num
            item['address']=address
            item['time']=time
            item['link']=link
            yield item
        print('爬取完毕',str(response.url))
        next_url=response.xpath('//tr[@class="f"]//a[@id="next"]/@href').extract_first()
        next_class=response.xpath('//tr[@class="f"]//a[@id="next"]/@class').extract_first()
        print(next_url,next_class)
        if not next_class:
            next_url='https://hr.tencent.com/'+next_url
            yield scrapy.Request(next_url,callback=self.parse)
        else:
            return

