from scrapy import Spider, Request

class DepokSpider(Spider):
    name="depok"
    start_urls = []
    for i in range(1,18):
        start_urls.append('http://jdih.depok.go.id/page/produk_hukum/11/'+str(i))
    for j in range(1,25):
        start_urls.append('http://jdih.depok.go.id/page/produk_hukum/12/'+str(j))
    
    def parse(self, response):
        for row in response.css('div#boxshadow>a.catg_title'):
            yield{
                'peraturan':row.css('h4>span::text').get()
            }
        # next_url = response.css("li.page-item>span.page-link>a::attr(href)")[17].get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)