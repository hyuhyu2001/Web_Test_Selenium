#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com, https://shop60459643.taobao.com/
@others:     © 2015 DTStudio, All rights reserved-- Created on 2016/11/09
@desc:
"""
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.baidu.com"
        self.driver.get(self.base_url + "/")
        self.search_text = self.driver.find_element_by_id("kw")
        self.search_btn = self.driver.find_element_by_id("su")


    def tearDown(self):
        # close the browser window
        self.driver.quit()
