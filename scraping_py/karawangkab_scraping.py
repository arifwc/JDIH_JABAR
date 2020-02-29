from scrapy import Spider, Request
import re

class KarawangKabSpider(Spider):
    name="KarawangKab"
    start_urls = []
    for i in range(1,140):
        start_urls.append('https://jdih.karawangkab.go.id/prokum-d?page='+str(i))
    
    def parse(self, response):
        for row in response.css('td.views-field'):
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css('.views-field-field-judul-ph-daerah::text').get()))
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)