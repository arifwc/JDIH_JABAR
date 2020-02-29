from scrapy import Spider, Request
import re

class CiamisSpider(Spider):
    name="Ciamis"
    
    start_urls = []
    for i in range(2000,2019):
        start_urls.append('https://jdih.ciamiskab.go.id/pusat/tahun-'+str(i))
    for j in range(2000,2020):
        start_urls.append('https://jdih.ciamiskab.go.id/perbup/'+str(j)+"-2/")
    
    def parse(self, response):
        for row in response.css('div.sdm_download_title'):
            yield{
                'peraturan':row.css('::text').get() 
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)