#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/08/25
@desc:
"""
from selenium import webdriver
import unittest
import time
from public_web.baselog import get_logger

log = get_logger()


class TestSearch(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(1, 1)
        log.info('info msg')

    def test_fail(self):
        self.assertEqual(1, 2, '1不等于2')
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     self.base_url = "http://www.baidu.com"
    #
    # def test_baidu(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("unittest")
    #     driver.find_element_by_id("su").click()
    #
    #     time.sleep(2)
    #     title = driver.title
    #     self.assertEqual(title, u"unittest_百度搜索")
    #
    # def tearDown(self):
    #     self.driver.quit()


if __name__ == "__main__":
    unittest.main()
