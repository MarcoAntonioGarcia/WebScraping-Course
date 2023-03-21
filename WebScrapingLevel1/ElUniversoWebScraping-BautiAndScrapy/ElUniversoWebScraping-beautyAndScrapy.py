from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


#Here we have the class which is named like the request and it have the atributes, this atribustes are
#fields which represent the extractions of data
class Notice (Item): 
    id =Field()
    title = Field()
    #description = Field()

class ElUniversoSpider(Spider):
    name="MySecondSpider"
    custom_settings={
        'USER_AGENT': "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    start_urls=['https://www.eluniverso.com/deportes/']

    #SI QUEREMOS USAR SCRAPY
    
    def parse(self, response):
        selector=Selector(response)
        Notices=selector.xpath('//div[contains(@class,"region") and contains(@class,"region-content" )]//div[contains(@class,"chain") and contains(@class,"chain-section" )]//ul[contains(@class, "feed") and contains(@class, "divide-y relative")]//li[@class="relative"]')
        i=0
        for notice in Notices:
            item=ItemLoader(Notice(), notice) 
            item.add_value('id', i)
            item.add_xpath('title', './/h2/a/text()')
            #item.add_xpath('description', './/p[contains(@class,"summary")]/text()')
            i+=1
            yield item.load_item()
            
    
    """
    #USANDO BAUTIFULSOAP
    def parse(self, response):
        soup=BeautifulSoup(response.body)
        notices_container = soup.find_all('div', class_='region')
        for container in notices_container:
            notice=container.find_all('div',class_='chain', recursive=False)
            for no in notice:
                item= ItemLoader(Notice(), response.body)
                titular =no.find('h2')
                #description=no.find('p')

                item.add_value('title', titular)
                #item.add_value('description', '')
                """

process=CrawlerProcess({
    'FEED_FORMAT':'csv',
    'FEED_URI': 'Response.csv'
})
process.crawl(ElUniversoSpider)
process.start()

                               
                               