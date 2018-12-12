#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import random
import ProxyPool.config

class RedisClient(object):
    """
    Redis Client
    """

    def __init__(self, host, port, password):
