#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from multiprocessing import Process

from test.tester import Tester
from getter.getter import Getter
from api.api import app

TEST_TIMES = 20
TESTER = True
GETTER = True
API = True


class Scheduler():
    def scheduler_tester(self, cycle=TEST_TIMES):
        tester = Tester()
        while True:
            tester.run()
            time.sleep(cycle)

    def scheduler_getter(self, cycle=TEST_TIMES):
        getter = Getter()
        while True:
            getter.run()
            time.sleep(cycle)

    def scheduler_api(self):
        app.run('127.0.0.1', 8000)

    def run(self):
        print('running...')
        if TESTER:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()
        if GETTER:
            getter_process = Process(target=self.scheduler_getter)
            getter_process.start()
        if API:
            api_process = Process(target=self.scheduler_api)
            api_process.start()