#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.110 Safari/537.36 ',
    'Host': 'www.xicidaili.com'
}


def request(url, **kwargs):
    """
    请求代理地址
    :param url:
    :param options:
    :return:
    """
    headers.update(headers, **kwargs)
    print('正在抓取{}'.format(url))
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except Exception:
        print('请求失败{}'.format(url))
        return None
