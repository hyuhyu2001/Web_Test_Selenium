#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:      使用xml文件存储测试数据
"""
import time
import xml.dom.minidom
import os
from selenium import webdriver

project_dir = os.getcwd()
fpath = project_dir.split('test_case')[0] + 'test_data' + os.sep + 'test_xml.xml'

# 打开 xml 文档
dom = xml.dom.minidom.parse(fpath)

# 得到文档元素对象
root = dom.documentElement

url = root.getElementsByTagName('register_page')
reg_page = url[0].firstChild.data

users = root.getElementsByTagName('user')
# 获得 null 标签的 username、password 属性值
username = users[0].getAttribute("username")
email = users[0].getAttribute("email")

dr = webdriver.Firefox()
dr.maximize_window()
dr.implicitly_wait(30)
dr.get(reg_page)

dr.find_element_by_name("username").clear()
dr.find_element_by_name("username").send_keys(username)
dr.find_element_by_name("email").clear()
dr.find_element_by_name("email").send_keys(email)
time.sleep(3)

dr.quit()