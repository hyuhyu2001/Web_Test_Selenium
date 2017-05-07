#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     dingyj
@contact:    june.diny@gmail.com, https://shop60459643.taobao.com/
@others:     DTStudio, All rights reserved-- Created on 2016/11/9
@desc:
"""
import unittest
import time
from .base.basetestcase import BaseTestCase


class SearchTest(BaseTestCase):
    def test_search_btn_displayed(self):
        self.assertTrue(self.search_btn.is_displayed())
        self.assertTrue(self.search_btn.is_enabled())

    def test_search_text_maxlength(self):
        max_length = self.search_text.get_attribute("maxlength")
        self.assertEqual("255", max_length)

    def test_search(self):
        self.search_text.clear()
        self.search_text.send_keys("unittest")
        self.search_btn.click()

        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, u"unittest_百度搜索")


if __name__ == '__main__':
    unittest.main(verbosity=3)


