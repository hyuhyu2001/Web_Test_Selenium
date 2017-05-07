#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:       如何处理ajax等异步加载的情形？
2种处理：1.利用webdriver的等待--显示等待和隐式等待；2.硬性等待time.sleep
"""
import time
from selenium import webdriver
# 要记住常用的这些方法在哪个模块里面
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.maximize_window()

# 【webdriver隐式等待】， implicitly_wait默认是0秒，
# implicitly_wait不针对特定元素做等待，它是等待整个页面加载完成。
# 当执行到find_element时，如果找到，继续执行；如果没找到，就不断地轮训查找元素，直到超时
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

try:
    input_ = driver.find_element_by_id("kw22")
except NoSuchElementException as e:
    print("The element is not present!!! ", e)

# Output: The element is not present!!!  Message: Unable to locate element: {"method":"id","selector":"kw22"}


# 【webdriver显示等待】：根据页面某个特定元素，来决定下一步动作；
# 每隔0.5秒检查一次，超时时长为5秒钟
element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID, "kw")))

# WebDriverWait有until和until_not 2个方法，参考wait.py
# expected_conditions里有很多方法，参考expected_conditions.py

element.send_keys('selenium')

btn = driver.find_element_by_id("su")
btn.click()
# 【time.sleep硬性等待】，脚本不执行任何动作，就是等10秒钟再执行下一步
# 不建议使用
time.sleep(10)

driver.quit()

