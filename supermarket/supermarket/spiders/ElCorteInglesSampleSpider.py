import scrapy

from ..items import SupermarketItem


class ElCorteInglesSampleSpider(scrapy.Spider):
    name = "elcorteinglessample"
    start_urls = {
        'https://www.elcorteingles.pt/animais/gato/racao-seca/'
    }

    def parse(self, response):
        items = SupermarketItem()

        for item in response.css('div.grid-item'):
            items['image_url'] = item.css('.js-lazy-load::attr(data-src)').extract()

            items['name'] = item.css('.link::text').extract()
            # items['brand'] = item.css('.product-item-brand::text').extract()[0].strip()
            # items['subtitle'] = item.css('.product-item-quantity-price::text').extract()[0].strip()
            price = item.css('div[class="prices-price _current"]').css('span::text').extract()
            items['price_now'] = "{}.{}".format(price[0], price[1])
            # items['price_before'] = price
            items['discount'] = 0
            yield items
