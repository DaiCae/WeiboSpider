# -*- coding: utf-8 -*-
import datetime
import json
import os.path
import time

import pika


class JsonWriterPipeline(object):
    """
    写入json文件的pipline
    """

    def __init__(self):
        self.file = None
        if not os.path.exists('../output'):
            os.mkdir('../output')

    def process_item(self, item, spider):
        """
        处理item
        """
        if not self.file:
            file_name = spider.name + '.jsonl'
            self.file = open(f'output/{file_name}', 'wt', encoding='utf-8')
        item['crawl_time'] = int(time.time())
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        self.file.flush()
        return item


class RabitMQSenderPipeline(object):
    def __init__(self):
        # 连接队列服务器
        root = pika.PlainCredentials("root", "123456")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='master', credentials=root))
        channel = connection.channel()
        # 初始化队列
        channel.queue_declare(queue="postQueue", durable=True)
        channel.queue_declare(queue="commentQueue", durable=True)
        self.channel = channel

    def process_item(self, item, spider):
        """
        处理item
        """
        item['crawl_time'] = int(time.time())
        channel = self.channel

        routing_key = None
        if "search" in spider.name:
            routing_key = "postQueue"
        elif "comment" in spider.name:
            routing_key = "commentQueue"

        if routing_key is not None:
            message = json.dumps(dict(item), ensure_ascii=False).encode("utf-8")
            channel.basic_publish(exchange='', routing_key=routing_key, body=message)
        return item
