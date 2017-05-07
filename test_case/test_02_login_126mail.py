#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:       登陆126邮箱
"""
from selenium import webdriver
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("xxxxx")    # 输入你的邮箱账号
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("xxxxx")   # 输入你的邮箱密码
        driver.find_element_by_id("loginBtn").click()
        # 获取断言信息进行断言
        text = driver.find_element_by_id("spnUid").text
        self.assertEqual(text, "xxxxx@126.com")   # 这里替换成你的邮箱地址
        # 退出
        driver.find_element_by_link_text(u"退出").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()