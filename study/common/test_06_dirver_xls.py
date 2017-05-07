#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/12
@desc:      使用标准excel文件存储测试数据
"""
import os
import time
import xlrd
from selenium import webdriver

project_dir = os.getcwd()
data_path = project_dir.split('test_case')[0] + os.sep + 'test_data' + os.sep + 'test_xls.xlsx'


def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    # 读取第一个sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

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

