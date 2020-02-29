from scrapy import Spider, Request

class BekasiSpider(Spider):
    name="bekasi"
    start_urls = [
        'https://jdih.bekasikota.go.id/peraturan-daerah',
        'https://jdih.bekasikota.go.id/peraturan-walikota'
        ]
    
    def parse(self, response):
        for row in response.xpath('//*[@class="table table-striped table-bordered"]//tbody//tr'):
            yield{
                'peraturan':row.xpath('td//text()')[1].extract()
                }
        next_url = response.css("li.next > a::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)