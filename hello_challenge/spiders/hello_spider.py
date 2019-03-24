import scrapy
from scrapy.http import FormRequest
import functools

class HelloSpider(scrapy.Spider):
    name = "hello_tree"
    start_urls = ['https://www.drukzo.nl.joao.hlop.nl/python.php']

    def parse(self, response, id=None, value=None):
        option = value

        id = response.css('select::attr(id)').extract()[-1]
        values = response.xpath('//select[@id="%s"]/option/@value' %(id)).extract()
        
        for value in values:       
            form_data = {'%s' %(id): value, 'value': 'submit'}

            yield {'option': option, 'id': id, 'value': value}
            
            yield FormRequest.from_response(response, 
                                            formdata=form_data,
                                            callback=functools.partial(self.parse, id=id, value=value)
                                            )
        


