#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:       测试126邮箱的登陆功能
1.使用公共方法public.login
2.将测试数据放在xml文件中，使用数据驱动(/test_data/login.xml)
3.这里使用xml.dom.minidom读取xml数据，作为扩展学习，建议大家具体看下
"""
import unittest
import xml.dom.minidom
import os
import sys
from selenium import webdriver

cur_dir = os.getcwd()
sys.path.append(cur_dir.split(r'\test_case')[0])

from public_web import login

fpath = cur_dir.split('test_case')[0] + 'test_data' + os.sep + 'login.xml'

# 打开 xml 文档
dom = xml.dom.minidom.parse(fpath)

# 得到文档元素对象
root = dom.documentElement


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []

    # 用例1：用户名、密码为空
    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        # 读取xml中的数据
        logins = root.getElementsByTagName('null')
        # 获得 null 标签的 username、password 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text, prompt_info)

    # 用例2：用户名为空
    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('user_null')
        # 获得 user_null 标签的 username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text, prompt_info)

    # 用例3：密码为空
    def test_pwd_null(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('pwd_null')
        # 获得 pwd_null 标签的 username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text, prompt_info)

    # 用例4：错误的用户名和密码
    def test_error(self):
        driver = self.driver
        driver.get(self.base_url)
        logins = root.getElementsByTagName('error')
        # 获得 error 标签的 username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
        self.assertEqual(text, prompt_info)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()