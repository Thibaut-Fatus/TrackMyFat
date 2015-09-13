# -*- coding: utf-8 -*-

# Scrapy settings for macdo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'macdo'

SPIDER_MODULES = ['back.scraper.macdo.spiders']
NEWSPIDER_MODULE = 'back.scraper.macdo.spiders'
LOG_LEVEL = 'INFO'
ITEM_PIPELINES = {
        'back.scraper.macdo.pipelines.MacdoPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'bobby is crawling products information'
