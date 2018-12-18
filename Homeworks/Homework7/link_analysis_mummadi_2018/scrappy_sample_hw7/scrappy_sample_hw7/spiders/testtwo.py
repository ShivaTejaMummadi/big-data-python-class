from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrappy_sample_hw7.items import SteamlistSampleItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class gamertripitem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    response = scrapy.Field()
    
class gamertripSpider(scrapy.Spider):
    name = 'steam'
    allowed_domains = ['https://www.engadget.com/']
    start_urls = ['https://www.engadget.com/gaming/',
	'https://www.engadget.com/entertainment/','https://www.engadget.com/gear/','https://www.engadget.com/buyers-guide/'
                  ]
    rules = (Rule(SgmlLinkExtractor(allow=(),restrict_xpaths=('//a[@class="button next"]',)),
                  callback="parse", 
                  follow= True),)



    def parse(self, response):
        hxs = scrapy.Selector(response)
        titles = hxs.xpath('//ul/li')
        item = []
        for title in titles:
            item_object = gamertripitem()
            item_object["title"] = title.xpath("a/text()").extract()
            item_object["link"] = title.xpath("a/@href").extract()
            item_object["response"] = response
            if item_object["title"] != []:
                item.append(item_object)

        return item