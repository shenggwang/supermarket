import scrapy

import supermarket.utils.math
from ..items import SupermarketItem

class AuchanSpider(scrapy.Spider):
    name = "auchan"
    # pagination 15 - 90
    start_urls = {
        'https://www.auchan.pt/Frontoffice/animais/gato/racao_para_gatos'
    }

    def parse(self, response):
        items = SupermarketItem()

        ProductItems = response.xpath('//*[(@id = "DivWrapperProductItem")]').extract()
        file = open('results/auchan.txt', 'wb')
        file.write(ProductItems)
        for item in ProductItems.css('div.divDataList'):
            print('inside for')
            # items['image'] = item.css('.lazy .lazy selectorgadget_selected')
            items['name'] = item.css('.selectorgadget_selected::text').extract()[0].strip()
            print(items['name'])
            print('debug')
            # items['type'] = item.css('.product-item-brand::text').extract()[0].strip()
            # items['subtitle'] = item.css('.product-item-quantity-price::text').extract()[0].strip()
            prices = item.css('.product-item-price .selectorgadget_selected::text').extract()
            print(prices)
            if len(prices) > 1:
                now = float(prices[0].strip('€ ').replace(',', '.').strip())
                before = float(prices[1].strip('€ ').replace(',', '.').strip())
                items['price_now'] = now
                items['price_before'] = before
                items['discount'] = math.getPercentage(now, before)
            else:
                items['price_now'] = float(prices[0].strip('€ ').replace(',', '.').strip())
                items['price_before'] = float(prices[0].strip('€ ').replace(',', '.').strip())
                items['discount'] = 0
            yield items
