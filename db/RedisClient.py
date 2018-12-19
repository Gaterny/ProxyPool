#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import random


MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10


class RedisClient(object):
    """
    Redis Client
    """

    def __init__(self):
        self.host = 'localhost'
        self.port = '6379'
        self.password = None
        self.name = 'proxies'

        self.db = redis.StrictRedis(host=self.host, port=self.port, password=self.password)

    def put(self, proxy, score=INITIAL_SCORE):
        """
        添加代理， 设置分数
        :param proxy: 代理
        :param score: 分数
        :return:
        """
        if not self.db.zscore(self.name, proxy):
            return self.db.zadd(self.name, score, proxy)

    def random(self):
        """
        随记获取代理，首先考虑分数最高的，其次考虑前一百
        :return: 代理
        """
        rank = self.db.zrangebyscore(self.name, MAX_SCORE, MIN_SCORE)
        if rank is not None:
            return random.choice(rank)
        else:
            rank = self.db.zrange(self.name, 0, 50)
            if rank is not None:
                return random.choice(rank)
            else:
                raise Exception

    def max(self, proxy):
        """
        判断可用，分数设置为100
        :param proxy:
        :return:
        """
        print('代理{}可用，设置为{}', proxy, MAX_SCORE)
        return self.db.zadd(self.name, MAX_SCORE, proxy)

    def decrease(self, proxy):
        """
        检测代理是否可用，不可用，分数减2，分数为0时抛弃
        :param proxy:
        :return:
        """
        score = self.db.zscore(self.name, proxy)
        if score and score > MIN_SCORE:
            print('当前代理{}不可用，当前分数{}减2', proxy, score)
            return self.db.zincrby(self.name, proxy, -2)
        else:
            print('当前代理{}分数为{}，抛弃'.format(proxy, score))
            return self.db.zrem(self.name, proxy)

    def exists(self, proxy):
        """
        判断代理是否存在数据库
        :param proxy:
        :return:
        """
        if self.db.zscore(self.name, proxy):
            return True
        else:
            return False

    def count(self):
        """
        获取代理数量
        :return:
        """
        return self.db.zcard(self.name)

    def all(self):
        """
        获取全部代理
        :return:
        """
        return self.db.zscan(self.name)