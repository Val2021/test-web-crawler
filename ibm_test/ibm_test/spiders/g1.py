import scrapy

class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):
        urls = response.xpath("//a/@href").getall()
        for url in urls:
            yield{
                "url":url
            }
       
  

