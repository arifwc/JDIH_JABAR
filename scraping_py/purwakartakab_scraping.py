from scrapy import Spider, Request

class PurwakartaKabSpider(Spider):
    name="PurwakartaKab"
    start_urls = [
        'https://jdih.purwakartakab.go.id/p/peraturan-daerah',
        'https://jdih.purwakartakab.go.id/p/peraturan-bupati',
        'https://jdih.purwakartakab.go.id/p/keputusan-bupati'
        ]
    
    def parse(self, response):
        for row in response.css("p"):
            yield{
                'peraturan':row.css("::text").get()
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)