from scrapy.item import Item, Field

class SteamlistSampleItem(Item):
    title = Field()
    link = Field()