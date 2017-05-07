#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:       模拟鼠标右键、双击、悬停、拖动，该如何操作呢？
在 WebDriver 中，关于鼠标操作的方法由 ActionChains 类提供。
ActionChains 类提供的鼠标操作的常用方法：
1. context_click() 右击
2. double_click() 双击
3. drag_and_drop() 拖动
4. move_to_element() 鼠标悬停
5. perform() 执行所有 ActionChains 中存储的行为
建议大家看下action_chains.py的源码
"""
import unittest
import time
from .base.basetestcase import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseOperation(BaseTestCase):
    def test_move_to_element(self):
        driver = self.driver
        # 鼠标悬停到"设置"上之后，显示一个下拉菜单，里面包含搜索的一些设置选项
        setting_item = driver.find_element_by_link_text(u'设置')
        ActionChains(driver).move_to_element(setting_item).perform()
        # print setting_item.get_attribute("class")
        # time.sleep(10)
        search_setting = driver.find_element_by_class_name("setpref")
        self.assertTrue(search_setting.is_enabled())
        self.assertEqual(u"搜索设置", search_setting.text)

    def test_double_click(self):
        """例子请大家补充"""
        pass
        # driver = self.driver
        # setting_item =driver.find_element_by_id("xx")
        # #对定位到的元素执行鼠标双击操作
        # ActionChains(driver).double_click(setting_item).perform()

    def test_right_click(self):
        """例子请大家补充"""
        pass
        # driver = self.driver
        # setting_item =driver.find_element_by_id("xx")
        # ActionChains(driver).context_click(setting_item).perform()

    def test_drag_and_drop(self):
        """例子请大家补充"""
        pass
        # driver = self.driver
        # 源位置
        # start_element = driver.find_element_by_name("xxx")
        # 要移动到的目标位置
        # target_element = driver.find_element_by_name("xxx")
        # ActionChains(driver).drag_and_drop(start_element, target_element).perform()


if __name__ == '__main__':
    unittest.main(verbosity=3)