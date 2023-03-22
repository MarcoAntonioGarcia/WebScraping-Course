from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule #to use vertical WebScraping
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

class Hotel(Item): 
    #id = Field()
    A_name =Field()
    B_cost = Field()
    #description = Field()
    #C_amenities = Field() 

class TripHotel (CrawlSpider):
    name="Hotel"
    custom_settings={
        'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    start_urls=['https://www.tripadvisor.com.mx/Hotels-g150807-Cancun_Yucatan_Peninsula-Hotels.html']
    downloand_delay=2 #time delay for don't give a banish from somepages

    rules =(
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ),follow=False, callback="parse_hotel" #nombre de la funcion donde van los items, esta funcion se llamara cuando los 
                  #links cumplan con la regla donde se especifica
        ),
    ) 

    def deleteDolarSimbol(self, texto):
        newText=texto.replace("$","")
        return newText


    def parse_hotel(self, response):
        selector =Selector(response)
        item = ItemLoader(Hotel(), selector)
        item.add_xpath('A_name', '//h1[@id="HEADING"]/text()')
        item.add_xpath('B_cost','//a[contains(@class ,"bookableOffer")]/div[1]/div[2]/div/text()', MapCompose(self.deleteDolarSimbol))
        #item.add_xpath('description','//div')
        #item.add_xpath('C_amenities','//div[contains(@class, "yplav f ME H3 _c")]/text()' )
        yield item.load_item()


#scrapy runspider TripadvisorWebScraping.py -o testscrapy.csv -t csv 
#//*[@id="bor_book_link_40791816"]/div[1]/div[2]/div