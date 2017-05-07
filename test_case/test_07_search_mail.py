#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:        search in mail box
"""
import unittest
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cur_dir = os.getcwd()
sys.path.append(cur_dir.split(r'\test_case')[0])

from public_web import login



class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 搜索邮件
    def test_search_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        # 调用登录模块
        login.login(self, 'xxxx', 'xxxx')
        # 搜索邮件
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(u'小明')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        #断言搜索邮件标签页面
        text = driver.find_element_by_xpath("//div[@id='dvMultiTab']/ul/li[5]/div[3]").text
        self.assertEqual(text, u'搜索邮件')
        #调用退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()