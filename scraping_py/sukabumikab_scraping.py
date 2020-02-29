from scrapy import Spider, Request
import re

class SukabumiSpider(Spider):
    name="Sukabumi"
    start_urls = [
        'http://jdih.sukabumikab.go.id/v1/peraturan/sukabumikab'
        ]
    
    def parse(self, response):
        for row in response.css("table#example>tbody>tr"):
            yield{
                'peraturan':re.sub(r"\s+"," ",str(row.css("td>a::text").get()))
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)