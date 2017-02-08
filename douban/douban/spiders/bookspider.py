# -*- coding:utf-8 -*-
'''by sudo rm -rf  http://imchenkun.com'''
import scrapy
from douban.douban.items import DoubanBookItem


class BookSpider(scrapy.Spider):
    name = 'douban-book'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://book.douban.com/top250'
    ]

    def parse(self, response):
        # 请求第一页
        #在不同的抓取级别的request之间传递参数的办法：目的是抓取所有页面的内容
        yield scrapy.Request(response.url, callback=self.parse_next)

        # 请求其它页
        for page in response.xpath('//div[@class="paginator"]/a'):#所有page在页面的css选择器信息
            link = page.xpath('@href').extract()[0]#.extract是获取页面的meta
            print link
            # callback:请求参数，给请求参数附加数据，为待爬字段
            yield scrapy.Request(link, callback=self.parse_next)

    def parse_next(self, response):
        for item in response.xpath('//tr[@class="item"]'):
            book = DoubanBookItem()
            book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            book['price'] = item.xpath('td[2]/p/text()').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            yield book