# -*- coding: utf-8 -*-
#清理已抽取的实体

class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        info = item['price'].split(' / ')  # [法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元
        item['name'] = item['name']#依据显示格式抽取
        item['price'] = info[-1]
        item['edition_year'] = info[-2]
        item['publisher'] = info[-3]
        return item


class DoubanMailPipeline(object):
    def process_item(self, item, spider):
        item['title'] = item['title'].replace(' ', '').replace('\\n', '')
        return item