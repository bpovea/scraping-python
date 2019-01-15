from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item):
    pregunta = Field()
    votos = Field()
    respuestas = Field()
    vistas = Field()
    temas = Field()
    

    id = Field()

class StackOverflowSpider(Spider):
    name = "Spider"
    start_urls = ['https://es.stackoverflow.com/']

    def parse(self,response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div/div[contains(@class,"question-summary")]')
        #iterar por preguntas
        for i,p in enumerate(preguntas):
            item = ItemLoader(Pregunta(), p)
            item.add_xpath('pregunta','.//h3/a/text()')
            # info = p.xpath('.//div/div[@class="mini-counts"]/span/text()')
            # import ipdb; ipdb.set_trace()
            item.add_xpath('respuestas','.//div[contains(@class,"status")]/div/span/text()')
            item.add_xpath('votos','.//div[contains(@class,"votes")]/div/span/text()')
            item.add_xpath('vistas','.//div[contains(@class,"views")]/div/span/text()')
            tags = []
            for tag in p.xpath('.//a[@class="post-tag"]/text()').extract():
                tags.append(tag)
            item.add_value('temas',"/".join(tags))
            item.add_value('id',i)
            yield item.load_item()
         