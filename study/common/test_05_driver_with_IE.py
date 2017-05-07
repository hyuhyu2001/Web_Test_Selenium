#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     © 2015 DTStudio, All rights reserved-- Created on 2016/11/04
@desc:       search products by chrome driver
"""
import os

from selenium import webdriver

# 获取 chromedriver.exe 的完整路径
project_dir = os.getcwd().split(os.sep + 'test_case')[0]
ie_driver_path = project_dir + os.sep + 'driver_file' + os.sep + 'IEDriverServer.exe'

# 创建 Chrome session
driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# 打开创汇网校店铺搜索页
driver.get("https://shop60459643.taobao.com/search.htm")

# 获取店铺搜索输入框
search_field = driver.find_element_by_name("keyword")
search_field.clear()

# 输入关键字，提交
search_field.send_keys("python")
search_field.submit()

# 使用 find_element_by_xpath 获取搜索结果的汇总信息
results = driver.find_element_by_xpath(".//*[@id='shop-search-list']/div/div[2]")
print(results.text)
# 共搜索到 1 个符合条件的商品。

# 使用 find_elements_by_class_name 获取每一个商品的名称
products = driver.find_elements_by_class_name("item-name")
# 看下一共有多少个？  是不是和 results.text 结果一致？
print(u"共搜索到 " + str(len(products)) + u" 个符合条件的商品。")

# 注意：搜索结果有很多页的时候，len(products）肯定是小于results.txt中的统计数值的

# 遍历products，打印每一个商品的名称
for product in products:
    print(product.text)

# 退出浏览器，并关闭 IE session
driver.quit()


# 启动IE时，可能会遇到这样的提示：
# Unexpected error launching Internet Explorer. Protected Mode settings are not the same for all zones.
# Enable Protected Mode must be set to the same value (enabled or disabled) for all zones.
# 如何解决呢？
# 更改IE的internet选项->安全，将【Internet/本地Intranet/受信任的站定/受限制的站点】中的”启用保护模式“全部去掉勾，或者全部勾上。
