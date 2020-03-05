from scrapy import Spider, Request
import re

class MajalengkaKabSpider(Spider):
    name="MajalengkaKab"
    
    start_urls = ['http://jdih.cimahikota.go.id/dokumen']
    
    def parse(self, response):
        for row in response.css('table.table.table-striped>tbody>tr'):
            yield{
                'peraturan':row.css('td::text')[0].get() 
                }
        next_url = response.css("li.page-item.NEXT > a::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)