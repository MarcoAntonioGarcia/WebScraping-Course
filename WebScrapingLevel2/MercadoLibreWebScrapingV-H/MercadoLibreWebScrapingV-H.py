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
    A_title = Field()
    #B_cost = Field()
    #C_description = Field()

class MercadoLibre_VH (CrawlSpider):
    name="MercadoLibre"
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 100 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }


    start_urls=['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']
    allowed_domains = ['articulo.mercadolibre.com.ec', 'listado.mercadolibre.com.ec'] #Solo bajara info de estos dominios
    downloand_delay=1
    
    rules = (
        Rule( # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/_Desde_\d+' # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=True),
        Rule( # REGLA #2 => VERTICALIDAD AL DETALLE DE LOS PRODUCTOS
            LinkExtractor(
                allow=r'/MEC-' 
            ), follow=True, callback='parse_items'), # Al entrar al detalle de los productos, se llama al callback con la respuesta al requerimiento
    )

    def parse_items(self, response):

        item = ItemLoader(Article(), response)
        
        # Utilizo Map Compose con funciones anonimas
        # PARA INVESTIGAR: Que son las funciones anonimas en Python?
        item.add_xpath('A_title', '//h1/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        #item.add_xpath('C_descripcion', '//div[@class="ui-pdp-description"]/p/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        #item.add_xpath('B_cost', '//span[@class="andes-money-amount__fraction"]/text()')
        yield item.load_item()

        #scrapy runspider MercadoLibreWebScrapingV-H.py -o testscrapy.csv -t csv 

