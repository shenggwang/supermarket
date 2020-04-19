import scrapy

from ..items import SupermarketItem

class AuchanSpider(scrapy.Spider):
    name = "auchan"
    # pagination 15 - 90
    start_urls = {
        'https://www.auchan.pt/Frontoffice/animais/gato/racao_para_gatos'
    }

    def parse(self, response):
        items = SupermarketItem()

        for item in response.css('div.product-item-border'):
            items['image_url'] = item.css('.product-item-image::attr(src)').extract()

            items['name'] = item.css('h3::text').extract()[0].strip()
            items['brand'] = item.css('.product-item-brand::text').extract()[0].strip()
            items['subtitle'] = item.css('.product-item-quantity-price::text').extract()[0].strip()

            price = item.css('.product-item-price::text').extract()[0].replace('€', '').replace(',', '.').strip()
            items['price_now'] = price
            items['price_before'] = price
            items['discount'] = 0
            yield items
