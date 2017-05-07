#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/10
@desc:        多窗口切换
"""
import time
from selenium import webdriver


dr = webdriver.Firefox()
dr.implicitly_wait(10)
dr.maximize_window()
dr.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
main_window = dr.current_window_handle
dr.find_element_by_link_text(u'登录').click()
dr.find_element_by_link_text(u"立即注册").click()

#获得当前所有打开的窗口的句柄
all_handles = dr.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != main_window:
        dr.switch_to.window(handle)
        print(u'进入注册窗口！')
        dr.find_element_by_name("account").send_keys('username')
        dr.find_element_by_name('password').send_keys('password')
        time.sleep(3)

# # 方法1：进入搜索窗口
# for handle in all_handles:
#     if handle == main_window:
#         dr.switch_to.window(handle)
#         print u'进入搜索窗口！'
#         dr.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
#         dr.find_element_by_id("kw").send_keys("selenium")
#         dr.find_element_by_id("su").click()
#         time.sleep(3)

# 方法2：进入搜索窗口
# 前面已经将住页面的handle存入到main_window里，所以这里可以不用for循环来查找
dr.switch_to.window(main_window)
print(u'进入搜索窗口！')
dr.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
time.sleep(3)

dr.quit()