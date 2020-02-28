from scrapy import Spider, Request
import re

class CirebonKabSpider(Spider):
    name="CirebonKab"
    start_urls = []
    for h in range(0,150,10):
        start_urls.append('https://jdih.cirebonkab.go.id/prodkum.php?cat_id=7&rowstart7='+str(h))
    for i in range(0,310,10):
        start_urls.append('https://jdih.cirebonkab.go.id/prodkum.php?cat_id=8&rowstart8='+str(i))
    
    def parse(self, response):
        for row in response.css("tr>td.tbl1"):
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css("a::text").get()))
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)