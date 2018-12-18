import scrapy

class WeatherItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    resp = scrapy.Field()
    
class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com']
    start_urls = ['https://weather.com/']

    def parse(self, response):
        hxs = scrapy.Selector(response)
        titles = hxs.xpath('//ul/li')
        item = []
        for title in titles:
            obj = WeatherItem()
            obj["title"] = title.xpath("a/text()").extract()
            obj["link"] = title.xpath("a/@href").extract()
            obj["resp"] = response
            if obj["title"] != []:
                item.append(obj)

        return item