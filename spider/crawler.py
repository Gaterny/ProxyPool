#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.request import request
from lxml import etree


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    """
    代理抓取
    """
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('获取到代理{}'.format(proxy))
            proxies.append(proxy)
        return proxies

    def crawl_xici(self, page_num=5):
        """
        获取西刺代理，只获取前5页
        普通方法返回521，因为需要执行一段js代码，改为用selenium
        :return:
        """

        for page in range(1, page_num+1):
            url = 'https://www.xicidaili.com/nn/{}'.format(page)
            print('Crawling {}'.format(url))
            html = request(url)
            print(html)
            doc = etree.HTML(html)
            ip = doc.xpath('//tr/td[2]/text()')
            port = doc.xpath('//tr/td[3]/text()')
            for item in zip(ip, port):
                yield ":".join(item)




