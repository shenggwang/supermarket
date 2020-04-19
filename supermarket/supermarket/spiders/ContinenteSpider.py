import scrapy

import supermarket.utils.math
from ..items import SupermarketItem


class ContinenteSpider(scrapy.Spider):
    name = "continente"
    start_urls = {
        'https://www.continente.pt/stores/continente/pt-pt/public/Pages/subcategory.aspx?cat=animais-gato-racao-esteril#/?pl=100'
    }

    def parse(self, response):
        items = SupermarketItem()
        for item in response.css('div.productItem'):
            # items['image'] = item.css('.lazy .lazy selectorgadget_selected')
            items['name'] = item.css('.ecsf_QuerySuggestions::text').extract()[0].strip()
            items['type'] = item.css('.type::text').extract()[0].strip()
            items['subtitle'] = item.css('.subTitle::text').extract()[0].strip()
            prices = item.css('.priceFirstRow::text').extract()
            if len(prices) > 1:
                now = float(prices[0].strip('€ ').replace(',', '.'))
                before = float(prices[1].strip('€ ').replace(',', '.'))
                items['price_now'] = now
                items['price_before'] = before
                items['discount'] = math.getPercentage(now, before)
            else:
                items['price_now'] = float(prices[0].strip('€ ').replace(',', '.'))
                items['price_before'] = float(prices[0].strip('€ ').replace(',', '.'))
                items['discount'] = 0
            yield items
