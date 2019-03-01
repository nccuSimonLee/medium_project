# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MediumCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    reading_time = scrapy.Field()
    claps = scrapy.Field()
    content = scrapy.Field()
    pass
