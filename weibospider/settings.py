# -*- coding: utf-8 -*-

BOT_NAME = 'weibospider'

SPIDER_MODULES = ['weibospider.spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

with open('cookie.txt', 'rt', encoding='utf-8') as f:
    cookie = f.read().strip()
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': cookie
}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
    'weibospider.middlewares.IPProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'weibospider.pipelines.RabitMQSenderPipeline': 100,
    'weibospider.pipelines.JsonWriterPipeline': 300,
}
