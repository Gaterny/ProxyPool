#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiohttp
import time
from db.RedisClient import RedisClient


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def test_single(self, proxy):
        """
        测试代理可用性
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                true_proxy = 'http://' + proxy
                print('testing: ', proxy)
                url = 'http://www.baidu.com'
                async with session.get(url, proxy=true_proxy, timeout=10) as response:
                    if response.status == 200:
                        self.redis.max(proxy)
                    else:
                        self.redis.decrease(proxy)
            except Exception:
                print('请求失败',proxy)

    def run(self):
        try:
            proxies = self.redis.all()
            loop = aiohttp.asyncio.get_event_loop()
            size = 100
            for i in range(0, len(proxies), size):
                test_proxies = proxies[i:i+size]
                tasks = [self.test_single(proxy) for proxy in test_proxies]
                loop.run_until_complete(aiohttp.asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('Error: ', e.args)
