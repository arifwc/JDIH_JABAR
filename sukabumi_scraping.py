from scrapy import Spider, Request

class SukabumiSpider(Spider):
    name="Sukabumi"
    start_urls = [
        'http://jdih.sukabumikota.go.id/home/dokumen/peraturan-daerah',
        'http://jdih.sukabumikota.go.id/home/dokumen/peraturan-walikota',
        # 'http://jdih.sukabumikota.go.id/home/dokumen/keputusan-walikota'
        ]
    
    def parse(self, response):
        for row in response.css("table#example>tbody>tr"):
            yield{
                'peraturan':row.css("td::text")[2].get()
                }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)