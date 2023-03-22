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

class Article(Item): 
    #id = Field()
    A_name = Field()
    B_cost = Field()
    c_description = Field()

class MercadoLibre_VH (CrawlSpider):
    name="MercadoLibre"
    custom_settings={
        'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        'CLOSESPIDER_PAGECOUNT': 20 #Limita la cantidad de paginas de donde sacara informacion
    }
    start_urls=['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']
    downloand_delay=1