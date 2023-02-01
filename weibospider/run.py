import os
import uuid
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from weibospider.spiders.comment import CommentSpider
from weibospider.spiders.search import SearchSpider


def init():
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'weibospider.settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    return process


def run_search(keywords, start_time, end_time):
    spider_id = str(uuid.uuid1())
    process = init()
    process.crawl(SearchSpider, keywords, start_time, end_time, spider_id)
    process.start()
    return spider_id


def run_comment(tweet_ids):
    spider_id = str(uuid.uuid1())
    process = init()
    process.crawl(CommentSpider, tweet_ids, spider_id)
    process.start()
    return spider_id

#

if __name__ == '__main__':
    run_search(['疫情', '新冠'], '2023-01-04', '2023-01-04')
