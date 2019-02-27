# -*- coding: utf-8 -*-
import scrapy
from medium_crawler.items import MediumCrawlerItem
from scrapy_splash import SplashRequest

class MediumSpiderSpider(scrapy.Spider):
    name = 'medium_spider'
    allowed_domains = ['towardsdatascience.com']
    start_urls = ['https://towardsdatascience.com/']

    def start_requests(self):
        script = """
                function main(splash)
                    local num_scrolls = 10
                    local scroll_delay = 1.0

                    local scroll_to = splash:jsfunc("window.scrollTo")
                    local get_body_height = splash:jsfunc(
                        "function() {return document.body.scrollHeight;}"
                    )
                    assert(splash:go(splash.args.url))
                    splash:wait(splash.args.wait)

                    for _ = 1, num_scrolls do
                        scroll_to(0, get_body_height())
                        splash:wait(scroll_delay)
                    end
                    return splash:html()
                end
                """
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, meta={
                "splash": {
                    "args": {"lua_source": script, "wait": 2},
                    "endpoint": "execute",
                }
            })

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
        item = MediumCrawlerItem()
        item["title"] = title
        item["author"] = author
        item["date"] = date
        item["reading_time"] = reading_time
        item["url"] = response.url
        #item.content = content
        yield item
