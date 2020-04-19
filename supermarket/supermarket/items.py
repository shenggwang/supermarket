# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SupermarketItem(scrapy.Item):
    image = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    subtitle = scrapy.Field()
    price_now = scrapy.Field()
    price_before = scrapy.Field()
    discount = scrapy.Field()