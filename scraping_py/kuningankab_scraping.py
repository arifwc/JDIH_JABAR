from scrapy import Spider, Request
import re

class BanjarKotaSpider(Spider):
    name="BanjarKota"
    
    start_urls = ['http://jdih.kuningankab.go.id/himpunan-produk-hukum/peraturan-daerah',
                  'http://jdih.kuningankab.go.id/himpunan-produk-hukum/peraturan-bupati',
                  'http://jdih.kuningankab.go.id/himpunan-produk-hukum/keputusan-bupati']
    
    def parse(self, response):
        for row in response.css('td.views-field.views-field-title.table__cell'):
            yield{
                'peraturan':row.css('a::text').get() 
                }
        next_url = response.css("li.pager__item.pager__item--next.pager__item--text > a::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)