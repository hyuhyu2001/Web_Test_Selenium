#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:       操作cookie
webdriver 操作 cookie 的方法有：
1. get_cookies() 获得所有 cookie 信息
2. get_cookie(name) 返回有特定 name 值有 cookie 信息
3. add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值
4. delete_cookie(name) 删除特定(部分)的 cookie 信息
5. delete_all_cookies() 删除所有 cookie 信息
"""
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class CookiesTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    def test_store_cookie(self):
        driver = self.driver
        # get the Your language dropdown as instance of Select class
        select_language = \
            Select(self.driver.find_element_by_id("select-language"))

        # check default selected option is English
        self.assertEqual("ENGLISH",
                         select_language.first_selected_option.text)
        # store cookies should be none
        store_cookie = driver.get_cookie("store")
        self.assertEqual(None, store_cookie)

        # select an option using select_by_visible text
        select_language.select_by_visible_text("French")

        # store cookie should be populated with selected country
        store_cookie = driver.get_cookie("store")['value']
        self.assertEqual("french", store_cookie)

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
