import scrapy 

class MOHS_Spider(scrapy.Spider): 
    name = "mohs" 
    def start_requests(self): 
        start_urls = [
            'https://www.mohs.gov.mm/' 
        ]
    
    def parse(self, response): 
        pass 
        