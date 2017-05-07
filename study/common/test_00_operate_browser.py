#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/13
@desc:      操作浏览器
"""
from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.INFO)


baidu = "http://www.baidu.com"
dr = webdriver.Firefox()
dr.get(baidu)

dr.set_window_size(600, 800)
time.sleep(3)
logging.info(u"设置浏览器高度为 600x800")

dr.set_window_position(300, 300)
time.sleep(3)
logging.info(u"设置浏览器在屏幕上的停放位置为(300,300)")

dr.maximize_window()
logging.info(u"设置浏览器最大化")

dr.get("http://www.163.com")

dr.back()
logging.info(u"上一页：回到百度页面")

dr.forward()
logging.info(u"下一页：回到163页面")

dr.quit()
logging.info(u"浏览器退出")

logging.info(u"Selenium 更多的功能等待你探索，加油吧!")
