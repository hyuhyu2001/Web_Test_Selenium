#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:日志输出
python提供了logging模块给运行中的应用程序提供了一个标准的信息输出接口，他提供了basicConfig()方法用于基本信息的定义
开启debug模块，就可以捕捉到客户端向服务器发送的请求
"""

from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
'''basicConfig()开启的debug模式只能捕捉到客户端向服务器发送的post请求，无法获得服务器所返回的应答信息
后面学习selenium server在获取更详细的请求和应答信息'''
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.quit()