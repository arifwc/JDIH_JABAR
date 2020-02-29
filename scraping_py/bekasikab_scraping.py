from scrapy import Spider, Request
import re

class BekasiKabSpider(Spider):
    name="BekasiKab"
    
    start_urls = []
    for j in range(1,78):
        start_urls.append('http://jdih.bekasikab.go.id/halperundangans-'+str(j)+".html")
    
    def parse(self, response):
        try: 
            yield{
                'peraturan':re.findall(r"[^\s*].*[^\s*]",str(response.css('div.post-border-right::text')[2].get()))
            }
            for row in response.css('div.wrapper'):
                yield{
                    'peraturan':re.findall(r"[^\s*].*[^\s*]",str(row.css('::text')[8].get())) 
                    }
            
        except IndexError:
            return
        
        
        # next_url = response.css("li.next > a::attr(href)").get()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parse)