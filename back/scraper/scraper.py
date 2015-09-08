from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from back.scraper.macdo.spiders.macdo_spider import MacdoSpider


class Scraper(object):

    def __init__(self, sites=None):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        spider = MacdoSpider()
        process.crawl(spider)
        process.start()
