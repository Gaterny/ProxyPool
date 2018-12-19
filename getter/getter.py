#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db.RedisClient import RedisClient
from spider.crawler import Crawler


class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def limit(self, limit_num=500):
        """
        判断代理数量是否超过代理池设定值
        :param limit_num:
        :return:
        """
        if self.redis.count() >= limit_num:
            return True
        else:
            return False

    def run(self):
        print("Getter is running...")
        if not self.limit():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.put(proxy)
