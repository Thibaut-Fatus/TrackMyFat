# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from back.models import Meal


class MacdoPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        try:
            info = item['info'].xpath("//h3//span").extract()
            url = item['url']
            print title
            print url
            print info
            Meal(url, title, info).save()
            print "_________\n"

            return {'title': title, 'info': info}
        except IndexError:
            print "#### can't parse %t ####".format(t=title)
