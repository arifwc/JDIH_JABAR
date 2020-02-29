from scrapy import Spider, Request

class GarutKabSpider(Spider):
    name="GarutKab"
    start_urls = []
    for i in range(1,18):
        start_urls.append('http://jdih.GarutKab.go.id/page/produk_hukum/11/'+str(i))
    for j in range(1,25):
        start_urls.append('http://jdih.GarutKab.go.id/page/produk_hukum/12/'+str(j))
    for k in range(1,6):
        start_urls.append('http://jdih.GarutKab.go.id/page/produk_hukum/16/'+str(k))
    
    def parse(self, response):
        for row in response.css('div#boxshadow'):
            perat=[]
            for i in row.css('span::text'):
                perat.append(i.get())
            yield{
                'peraturan':''.join(perat)
            }
        # next_url = response.css("li.page-item>span.page-link>a::attr(href)")[17].get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)