#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com, https://shop60459643.taobao.com/
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:        重点学习unittest的用法
注意setUp/setUpClass，tearDown/tearDownClass的区别
① setUp():每个测试函数运行前运行
② tearDown():每个测试函数运行完后执行
③ setUpClass():必须使用@classmethod 装饰器,所有test运行前运行一次
④ tearDownClass():必须使用@classmethod装饰器,所有test运行完后运行一次

unittest还有一些不常用的装饰器：
@unittest.skip(reason):无条件跳过测试，reason描述为什么跳过测试
@unittest.skipif(conditition,reason):condititon为true时跳过测试
@unittest.skipunless(condition,reason):condition不是true时跳过测试
@unittest.expectedFailure:如果test失败了，这个test不计入失败的case数目
"""
import unittest
import time
from selenium import webdriver


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.base_url = "http://www.baidu.com"
        cls.driver.get(cls.base_url + "/")

        cls.search_text = cls.driver.find_element_by_id("kw")
        cls.search_btn = cls.driver.find_element_by_id("su")

    def test_search_btn_displayed(self):
        self.assertTrue(self.search_btn.is_displayed())
        self.assertTrue(self.search_btn.is_enabled())

    def test_search_text_maxlength(self):
        max_length = self.search_text.get_attribute("maxlength")
        self.assertEqual("255", max_length)

    def test_search(self):
        self.search_text.clear()
        self.search_text.send_keys("unittest")
        self.search_btn.click()

        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=3)


