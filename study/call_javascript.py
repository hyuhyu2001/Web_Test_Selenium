#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:调用javascript
webdriver提供了前进和后退的方法，但对于浏览滚动条没有提供相应的操作方法，在这种情况下，可以借助javascript来控制浏览器的滚动条
webdriver提供了execute_scipt()方法来执行javascript代码
"""

from selenium import webdriver
import time


def call_scroll(driver):
    #将页面滚动条拖动到底部
    js1="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js1)
    time.sleep(3)

    #将页面滚动条拖动到顶部
    js2="var q=document.documentElement.scrollTop=0"
    driver.execute_script(js2)
    time.sleep(3)

    driver.set_window_size(600,600)#设置浏览器窗口大小
    #设置浏览器窗口的滚动条位置
    js3 =  "window.scrollTo(100,450)" #设置浏览器窗口滚动条的水平和垂直位置
    driver.execute_script(js3)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")

    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    time.sleep(3)
    call_scroll(driver)