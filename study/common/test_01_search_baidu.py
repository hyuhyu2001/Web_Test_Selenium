#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com, https://shop60459643.taobao.com/
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:        百度搜索
"""
import unittest
import time
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.baidu.com"
        self.driver.get(self.base_url + "/")

        self.search_text = self.driver.find_element_by_id("kw")
        self.search_btn = self.driver.find_element_by_id("su")

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

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=3)


