import scrapy

class MacdoSpider(scrapy.Spider):
	name = "macdo"
	allowed_domains = ["mcdonalds.fr"]
	start_urls = ["http://www.mcdonalds.fr/produits/sandwichs"]

	def parse(self, response):
		for sel in response.selector.xpath("//ul[@class='products']//a[not(@class) or @class!='btn-zebra-yellow-33']/@href").extract():
			print sel
