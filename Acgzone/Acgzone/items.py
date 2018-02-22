# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AcgzoneItemLoader(ItemLoader):
    default_out_processor = TakeFirst()

class AcgzoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pan = scrapy.Field()
    code = scrapy.Field()
    site = scrapy.Field()

