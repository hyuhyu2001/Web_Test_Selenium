#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/9/25
@desc:       
"""


# 登陆
def login(self, username, password):
    driver = self.driver
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys(username)
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys(password)
    driver.find_element_by_id("loginBtn").click()


# 退出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"退出").click()