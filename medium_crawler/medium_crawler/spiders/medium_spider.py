# -*- coding: utf-8 -*-
import scrapy


class MediumSpiderSpider(scrapy.Spider):
    name = 'medium_spider'
    allowed_domains = ['towardsdatascience.com']
    start_urls = ['https://towardsdatascience.com/']

    def parse(self, response):
        print("Processing.." + response.url)
        posts = response.css(".u-borderLighter")
        for post in posts:
            url = post.attrib["href"]
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css("h1::text").extract()[0] # extract 回傳 list
        author = response.css(".ds-link::text").extract()[0]
        date = response.css(".ui-caption > time").attrib["datetime"]
        reading_time = response.css(".readingTime").attrib["title"]
        cotent = response.css(".postArticle-content > section")
