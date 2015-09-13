import scrapy
from scrapy.http import Request

LOG_LEVEL = 'INFO'


class MacdoSpider(scrapy.Spider):
    name = "macdo"
    allowed_domains = ["mcdonalds.fr"]
    start_urls = ["http://www.mcdonalds.fr/produits/sandwichs",
                  "http://www.mcdonalds.fr/produits/petite-faim"]

    def parse(self, response):
        for sel in response.selector.xpath("//ul[@class='products']//a[not(@class) or @class!='btn-zebra-yellow-33']/@href").extract():
            url = "http://www.mcdonalds.fr{url}".format(url=sel)
            yield Request(url, callback=self.parse_product)

    def parse_product(self, response):
        try:
            title = response.selector.xpath("//section[@role='main']//h1[@class='title head-wide']")[0].extract()
            sel = response.selector.xpath("//section[@class='info']")
            yield {'title': title,
                   'url': response.url,
                   'info': sel}
        except:
            return
