#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/18
@desc:
互联网技术越来越发达，目前大部分网页的下拉框都是通过div+css实现，很少使用基础的<select>标签
这里看下，该如何处理？
"""
import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = os.getcwd()
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'select.htm'
# path = 'file:///E:/selenium/mail126/demo_html/select.htm'
demo_page = path.decode('gbk').encode('utf-8')
print(demo_page)
br = webdriver.Firefox()
br.implicitly_wait(30)
br.maximize_window()
br.get(demo_page)

br.find_element_by_id("userName").clear()
br.find_element_by_id("userName").send_keys("QATEST")

# 方法一
br.find_element_by_id("companyType_value").click()
time.sleep(3)
# 物流企业
br.find_element_by_xpath(".//*[@id='companyTypeSelectDropDown']/ul/li[1]/a").click()
time.sleep(3)

# 方法二
br.find_element_by_id("companyType_value").click()
# 煤矿/洗煤厂/煤炭生产企业
element = WebDriverWait(br, 15, 0.5).until(
    EC.presence_of_element_located((By.XPATH, ".//*[@id='companyTypeSelectDropDown']/ul/li[2]/a")))
element.click()
time.sleep(3)

# 方法三
# 物流企业
js = 'document.getElementById("companyType_value").value="物流企业"'
br.execute_script(js)

time.sleep(3)
br.quit()