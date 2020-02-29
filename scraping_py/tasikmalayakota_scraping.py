from scrapy import Spider, Request
import re

class TasikmalayaKotaSpider(Spider):
    name="TasikmalayaKota"
    
    start_urls = ['https://jdih.tasikmalayakota.go.id/home/dokumen/perwal',
                  'https://jdih.tasikmalayakota.go.id/home/dokumen/perda']
    
    def parse(self, response):
        for row in response.css('div>bold'):
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css('::text').get()))
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)