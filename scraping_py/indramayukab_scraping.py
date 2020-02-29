from scrapy import Spider, Request
import re

class IndramayuKabSpider(Spider):
    name="IndramayuKab"
    start_urls = []
    for i in range(1,22):
        start_urls.append('http://jdih.indramayukab.go.id/index.php?p=produk-hukum-jenis&id=8&halaman='+str(i))
    for j in range(1,5):
        start_urls.append('http://jdih.indramayukab.go.id/index.php?p=produk-hukum-jenis&id=7&halaman='+str(j))
    
    def parse(self, response):
        for row in response.css('table.table.odd.produk>tr>td'):
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css('a::text').get()))
            }
        # next_url = response.css("li.page-item>span.page-link>a::attr(href)")[17].get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)