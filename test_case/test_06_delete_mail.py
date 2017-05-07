#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/9/29
@desc:        delete mail
我们多添加一些测试场景，比如：删除邮件，查找邮件，发送邮件等等
"""
import unittest
import os
import sys
from selenium import webdriver

cur_dir = os.getcwd()
sys.path.append(cur_dir.split(r'\test_case')[0])

from public_web import login


# from selenium.webdriver.common.keys import Keys
import time


class TestDel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 搜索邮件
    def test_del_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        # 调用登录模块
        login.login(self, 'xxxx', 'xxxx')
        # 打开收件箱
        driver.find_element_by_class_name('nui-tree-item-text').click()
        time.sleep(2)
        driver.find_elements_by_xpath("//span[@class='nui-chk-symbol']/b").pop(1).click()
        try:
            spans = driver.find_elements_by_tag_name('span')
            for s in spans:
                if s.text == u'删 除':
                    s.click()
        except:
            pass
        # 断言是否已删除
        text = driver.find_element_by_css_selector("span.nui-tips-text>a").text
        self.assertEqual(text, u'已删除')
        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()