from scrapy import Spider, Request

class BandungBaratKabSpider(Spider):
    name="BandungBaratKab"
    start_urls = [
        'https://jdih.bandungbaratkab.go.id/produkhukum/peraturan-daerah',
        'https://jdih.bandungbaratkab.go.id/produkhukum/peraturan-bupati'
        ]
    
    def parse(self, response):
        for row in response.css("table#example>tbody>tr"):
            yield{
                'peraturan':row.css("td::text")[3].get()
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)