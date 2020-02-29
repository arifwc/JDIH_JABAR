from scrapy import Spider, Request

class SumedangKabSpider(Spider):
    name="SumedangKab"
    start_urls = [
        'http://jdih.sumedangkab.go.id/index.php/front/aturan_perbup',
        'http://jdih.sumedangkab.go.id/index.php/front/aturan_perda',
        'http://jdih.sumedangkab.go.id/index.php/front/aturan_kepbup'
        ]
    
    def parse(self, response):
        if "perbup" in response.url:
            for row in response.css("table#sample_2>tbody>tr"):
                yield{
                    'peraturan':row.css("td::text")[2].get()
                    }
        else:
            for row in response.css("table#sample_1>tbody>tr"):
                if "perda" in response.url:
                    yield{
                        'peraturan':row.css("td::text")[2].get()
                        }
                else:
                    yield{
                        'peraturan':row.css("td::text")[3].get()
                        }
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)