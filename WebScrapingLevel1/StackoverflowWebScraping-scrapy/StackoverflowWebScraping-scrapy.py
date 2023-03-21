from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


#Here we have the class which is named like the request and it have the atributes, this atribustes are
#fields which represent the extractions of data
class Question (Item): 
    id =Field()
    question = Field()
    #description = Field()

class StackoverFlowSpider(Spider):
    name="MyFisrstSpider"
    custom_settings={
        'USER_AGENT': "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    start_urls=['https://stackoverflow.com/questions']

    def parse(self, response):
        selector=Selector(response)
        questions=selector.xpath('//div[@id="questions"]//div[contains(@class, "s-post-summary") and contains(@class, "js-post-summary")]')
        i=0
        for question in questions:
            #its giving the instance of class Question where we have the the fields to astract
            #the second parameter is from I give the information in this case is the iteration question
            item=ItemLoader(Question(), question) 
            item.add_xpath('question', './/h3/a/t ext()')
            #item.add_xpath('description', './/div[@class="s-post-summary--content-excerpt"]/text()')
            item.add_value('id', i)
            i+=1
            yield item.load_item()


