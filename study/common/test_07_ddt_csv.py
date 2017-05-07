#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/12
@desc:      使用ddt + csv 解压数据
ddt 不是Python的原生库，需要自己安装
"""

import unittest
import time
import csv
import os
from selenium import webdriver
from ddt import ddt, data, unpack

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


@ddt
class SearchDDTCsv(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://www.baidu.com/")

    # (search_value, expected_title)和装饰器@data里的数据是一一对应的
    # @data(("python", u"python_百度搜索"), ("unittest", u"unittest_百度搜索"))
    @data(*get_data(data_path))
    @unpack
    def test_search(self, search_value, expected_title):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_btn = self.driver.find_element_by_id("su")

        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_btn.click()

        time.sleep(3)

        # 从csv里面读取出来的不是unicode编码，所以expected_title要做一下转换
        expected_title = unicode(expected_title.decode('gbk'))
        title = self.driver.title
        self.assertEqual(expected_title, title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
