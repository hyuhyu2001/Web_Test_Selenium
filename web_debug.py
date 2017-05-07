#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
from selenium import webdriver

browser = webdriver.Firefox() #将Firefox对象赋值给变量brower
# browser = webdriver.Chrome()
# browser = webdriver.Ie()
browser.get("http://www.baidu.com")#get方法，可以向浏览器发送网址（URL）
browser.find_element_by_id("kw").send_keys('selenium2') #通过id=kw,定位到百度的输入框，并通过键盘输入方法send_keys()向百度输入框里输入搜索关键字'selenium2'
browser.find_element_by_id('su').click() #通过id=su定位“百度一下”搜索按钮
browser.quit()#退出并关闭浏览器及相关的驱动程序
