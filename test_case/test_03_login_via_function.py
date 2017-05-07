#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:       将登陆动作封装成function
"""
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 单独运行这个py文件时，需要加入下面的代码，用以将项目的目录加载到系统变量中。
# 使用all_test运行所有用例时，可以注释掉
cur_dir = os.getcwd()
sys.path.append(cur_dir.split(r'\test_case')[0])

from public_web import login


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        # self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        # 实际项目测试时，很多用例执行前都需要先登录账户，
        # 我们可以将这些常用的动作抽出来，组成一个function(/public/login.py)
        login.login(self, 'xxxxx', 'xxxxx')  # 输入你的邮箱账号和密码

        # 获取断言信息进行断言
        text = driver.find_element_by_id("spnUid").text
        self.assertEqual(text, "xxxxx@126.com")
        # 退出
        login.logout(self)

    # 搜索邮件
    def test_search_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        # 调用登录模块
        login.login(self, 'xxxxx', 'xxxxx')
        # 搜索邮件
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(u'小明')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        # 断言搜索邮件标签页面
        text = driver.find_element_by_xpath("//div[@id='dvMultiTab']/ul/li[5]/div[3]").text
        self.assertEqual(text, u'搜索邮件')
        # 调用退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    # unittest.main()
    import os
    print(os.getcwd())