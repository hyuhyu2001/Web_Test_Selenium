#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:       定制浏览器
"""
import unittest
import os
import time

from selenium import webdriver


class TestConfigFirefox(unittest.TestCase):
    def setUp(self):
        fp = webdriver.FirefoxProfile()

        # 在Firefox地址栏中输入about:config，查看相关配置属性
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", os.getcwd())
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                          "application/octet-stream")  # 下载文件的类型

        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()