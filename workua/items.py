# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PeopleItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()
    detail = scrapy.Field()