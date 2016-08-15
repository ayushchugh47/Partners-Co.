# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.http import FormRequest

class MySpider(scrapy.Spider):
    name = "ilsos"
    allowed_domains = ["ilsos.gov"]
    
    def start_requests(self):
        return [FormRequest(url="https://www.ilsos.gov/corporatellc/CorporateLlcController",method = 'POST',headers={'referer':'https://www.ilsos.gov/corporatellc/CorporateLlcController'},cookies={'JSESSIONID':'0001vEgNNSN8DRGdc7Tom1vjuxo:15rk6cbeg'},formdata={'command':'method','search':'startsWith','searchkeyword':'a'},callback = self.parse)]
    
    def parse(self, response):
        filename = 'MyResults.html'
        with open(filename, 'wb') as output:
            output.write(response.body)

