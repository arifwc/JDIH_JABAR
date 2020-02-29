from scrapy import Spider, Request
import re

class MajalengkaKabSpider(Spider):
    name="MajalengkaKab"
    
    start_urls = ['https://jdih.majalengkakab.go.id/index.php/web/result']
    
    def parse(self, response):
        for row in response.css('div.result__content__item__title'):
            yield{
                'peraturan':row.css('a::text').get() 
                }
        next_url = response.css("li.next > a::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)