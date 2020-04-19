import scrapy

from supermarket.utils import math
from ..items import SupermarketItem


class ContinenteSampleSpider(scrapy.Spider):
    name = "continentesample"
    start_urls = {
        'https://www.continente.pt/stores/continente/pt-pt/public/Pages/subcategory.aspx?cat=animais-gato-racao-esteril#/?pl=100'
    }

    def parse(self, response):
        items = SupermarketItem()
        for item in response.css('div.productItem'):
            items['image_url'] = item.css('.lazy::attr(data-original)').extract()
            # items['image_url'] = item.css('.lazy::attr(alt)').extract()
            items['name'] = item.css('.ecsf_QuerySuggestions::text').extract()[0].strip()
            items['brand'] = item.css('.type::text').extract()[0].strip()
            items['subtitle'] = item.css('.subTitle::text').extract()[0].strip()
            prices = item.css('.priceFirstRow::text').extract()
            if len(prices) > 1:
                now = float(prices[0].replace('€ ', '').replace(',', '.'))
                before = float(prices[1].replace('€ ', '').replace(',', '.'))
                items['price_now'] = now
                items['price_before'] = before
                items['discount'] = math.getPercentage(now, before)
            else:
                items['price_now'] = float(prices[0].replace('€ ', '').replace(',', '.'))
                items['price_before'] = float(prices[0].replace('€ ', '').replace(',', '.'))
                items['discount'] = 0
            yield items
