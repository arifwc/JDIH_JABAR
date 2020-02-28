from scrapy import Spider, Request
import re

class BanjarKotaSpider(Spider):
    name="BanjarKota"
    
    start_urls = ['https://jdih.banjarkota.go.id/produk-hukum-kategori/produk-hukum-daerah/peraturan-daerah/',
                  'https://jdih.banjarkota.go.id/produk-hukum-kategori/produk-hukum-daerah/peraturan-walikota/']
    
    def parse(self, response):
        for row in response.css('div.product_box'):
            yield{
                'peraturan':row.css('h2.woocommerce-loop-product__title::text').get() 
                }
        next_url = response.css("li > a.next.page-numbers::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)