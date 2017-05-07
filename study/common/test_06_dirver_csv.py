#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/12
@desc:      使用csv文件存储测试数据
"""
import os
import time
import csv
from selenium import webdriver

project_dir = os.getcwd()
data_path = project_dir.split('test_case')[0] + os.sep + 'test_data' + os.sep + 'test_csv.csv'


def get_data(file_name):
    rows = []
    data_file = open(file_name, "rb")
    reader = csv.reader(data_file)
    # 跳过测试文件中的第一行
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

# 通过csv.reader读出来的数据是list类型，还可以使用csv.DictReader来返回字典类型的数据
print(get_data(data_path))
for i in get_data(data_path):
    print(i)

dr = webdriver.Firefox()
dr.maximize_window()
dr.implicitly_wait(30)
dr.get("http://www.baidu.com")

for kw in get_data(data_path):
    dr.find_element_by_id("kw").clear()
    dr.find_element_by_id("kw").send_keys(kw[0])
    dr.find_element_by_id("su").click()
    time.sleep(3)

dr.quit()

# csv的其他用法，
