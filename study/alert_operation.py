#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:警告框处理：对于JavaScript生成的alert、confirm、以及prompt，使用方法switch_to_alert()定位到alert/confirm/prompt，然后使用text/accept/dismiss/send_keys等方法操作
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

d = webdriver.Firefox()
d.implicitly_wait(10)
d.get('https://www.baidu.com/')
d.maximize_window()

link = d.find_element_by_link_text('设置')
ActionChains(d).move_to_element(link).perform()#鼠标悬停至“设置”链接

d.find_element_by_link_text('搜索设置').click()#打开搜索设置
d.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)
#接受现有警告框
d.switch_to.alert().accept()
