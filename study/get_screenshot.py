#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:窗口截图，通过函数get_screenshot_as_file()来截取当前窗口
"""

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

#截取当前窗口，并执行截图图片的保存位置
driver.get_screenshot_as_file(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\baidu_img.jpg')