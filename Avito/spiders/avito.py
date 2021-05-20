import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from Avito.items import AvitoItem


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/kamyshin/nedvizhimost']

    def parse(self, response: HtmlResponse):
        ad_links = response.css('a.styles-link-36uWZ::attr(href)')
        for link in ad_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoItem(), response=response)

        loader.add_css('title',
                       'h1.title-info-title span.title-info-title-text::text')

        loader.add_css('images',
                       'div[class*="gallery-img-frame"]::attr(data-url)')

        loader.add_css('auto_params', 'li.item-params-list-item ::text')

        loader.add_value('url', response.url)

        yield loader.load_item()