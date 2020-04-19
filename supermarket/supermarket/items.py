# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SupermarketItem(scrapy.Item):
    image_url = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    subtitle = scrapy.Field()
    price_now = scrapy.Field()
    price_before = scrapy.Field()
    discount = scrapy.Field()