# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    words = scrapy.Field()
    pass
