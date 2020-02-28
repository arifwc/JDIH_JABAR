from scrapy import Spider, Request
import re

class BogorKabSpider(Spider):
    name="bogorkab"
    
    start_urls = []
    for i in range(1,71):
        start_urls.append('http://jdih.bogorkab.go.id/produk_hukum/all/page/'+str(i))
    
    def parse(self, response):
        for row in response.css('div.produk-info'):
            yield{
                'peraturan':row.css('div.produk-title>a::text').get() 
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)