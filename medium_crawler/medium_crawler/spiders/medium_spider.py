# -*- coding: utf-8 -*-
import scrapy


class MediumSpiderSpider(scrapy.Spider):
    name = 'medium_spider'
    allowed_domains = ['towardsdatascience.com']
    start_urls = ['https://towardsdatascience.com/']

    def parse(self, response):
        print("Processing.." + response.url)
        for res in response.css(".u-borderLighter"):
            print(res.attrib["href"])
