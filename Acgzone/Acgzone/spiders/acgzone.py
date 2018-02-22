# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from Acgzone.items import AcgzoneItem,AcgzoneItemLoader
from scrapy.loader import ItemLoader

class AcgzoneSpider(scrapy.Spider):
    name = 'acgzone'
    allowed_domains = ['www.uraban.me']
    start_urls = ['https://www.uraban.me/wp/']

    def parse(self, response):
        sites = response.xpath('//p/a/@href').extract()
        print(sites)
        for site in sites:
            yield Request(url=site,callback=self.parse_detail)

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first('')
        if next:
            yield Request(url=next_page,callback=self.parse)

    def parse_detail(self, response):
        acgzone_item = AcgzoneItem()
        item_loader = AcgzoneItemLoader(item=AcgzoneItem(),response=response)
        item_loader.add_xpath("title","//article/h1/a/text()")
        item_loader.add_xpath("pan","//blockquote/p/a/@href")
        item_loader.add_xpath("code","//blockquote/p/text()")
        item_loader.add_value("site",response.url)
        acgzone_item = item_loader.load_item()
        yield acgzone_item