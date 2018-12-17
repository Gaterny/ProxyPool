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
                attrs['__CrwalFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('获取到代理{}'.format(proxy))
            proxies.append(proxy)

    def crawl_daili66(self, page_num=10):
        """
        获取代理66，只获取前10页
        :return:
        """
        for page in range(1, page_num+1):
            url = 'http://www.66ip.cn/{}.html'.format(page)
            print('Crawling {}'.format(url))
            html = request(url)
            doc = etree.HTML(html)
            ip = doc.xpath('//tbody/tr/text()')




