from scrapy import Spider, Request
import re

class TasikmalayaKabSpider(Spider):
    name="TasikmalayaKab"
    
    start_urls = ['http://jdih.tasikmalayakab.go.id/?page=peraturan&act=listperaturan&id=81']
    
    def parse(self, response):
        for row in response.css('td.subjek'):
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css('::text').get()))
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)