#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:        如何模拟键盘操作呢？
键盘上的所有键在Keys类中都做了声明，请参看源码keys.py
"""
import unittest
import time
from .base.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestKeyboardOperation(BaseTestCase):
    def test_search(self):
        driver = self.driver
        # 思考：为什么在输入之前，都要执行clear操作呢？
        self.search_text.clear()
        self.search_text.send_keys("python")
        self.search_btn.click()
        self.assertEqual(driver.title, u"python_百度搜索")

    def test_keys_operation(self):
        driver = self.driver

        self.search_text.send_keys("pythonh")
        self.search_text.send_keys(Keys.BACK_SPACE)  # 删除最后一个"h"字符
        self.search_text.send_keys(Keys.CONTROL, 'a')    # Ctrl + A

        self.search_text.send_keys("selenium")
        self.search_btn.click()
        time.sleep(3)
        self.assertEqual(driver.title, u"selenium_百度搜索")

    def test_action_chains_key_operation(self):
        url = "https://rawgit.com/jeresig/jquery.hotkeys/master/test-static-05.html"
        driver = self.driver
        driver.get(url)
        driver.implicitly_wait(30)
        shift_n_label = WebDriverWait(self.driver, 10). \
            until(expected_conditions.visibility_of_element_located((By.ID, "_Shift_d")))

        # Shift+d，注意这里的用法
        ActionChains(driver).key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).perform()
        time.sleep(3)
        self.assertEqual("rgba(12, 162, 255, 1)",
                         shift_n_label.value_of_css_property("background-color"))


if __name__ == '__main__':
    unittest.main(verbosity=3)