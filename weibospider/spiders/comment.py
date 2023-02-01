#!/usr/bin/env python
# encoding: utf-8
"""
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2020/4/14
"""
import json
from scrapy import Spider
from scrapy.http import Request
from weibospider.spiders.common import parse_time, url_to_mid


class CommentSpider(Spider):
    """
    微博评论数据采集
    """
    name = "comment_"

    def __init__(self, tweet_ids, spider_id, **kwargs):
        super().__init__(**kwargs)
        self.tweet_ids = tweet_ids
        self.name = self.name + spider_id

    def start_requests(self):
        """
        爬虫入口
        """
        # 这里tweet_ids可替换成实际待采集的数据
        tweet_ids = self.tweet_ids
        for tweet_id in tweet_ids:
            mid = url_to_mid(tweet_id)
            url = f"https://weibo.com/ajax/statuses/buildComments?" \
                  f"is_reload=1&id={mid}&is_show_bulletin=2&is_mix=0&count=20"
            yield Request(url, callback=self.parse, meta={'source_url': url, "tweet_id": tweet_id})

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        data = json.loads(response.text)
        for comment_info in data['data']:
            item = self.parse_comment(comment_info,response.meta['tweet_id'])
            yield item
        if data.get('max_id', 0) != 0:
            url = response.meta['source_url'] + '&max_id=' + str(data['max_id'])
            yield Request(url, callback=self.parse, meta=response.meta)

    @staticmethod
    def parse_comment(data,tweet_id):
        """
        解析comment
        """
        item = dict()
        item['createdAt'] = parse_time(data['created_at'])
        item['_id'] = data['id']
        item['likeCounts'] = data['like_counts']
        item['ipLocation'] = data['source']
        item['content'] = data['text_raw']
        item['user'] = data['user']['screen_name']
        item['mblogid'] = tweet_id
        print(item)
        return item
