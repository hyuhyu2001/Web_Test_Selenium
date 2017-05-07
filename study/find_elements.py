#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:定位一组元素：在单词element后面加s表示复数，比如find_elements_by_id  ,也支持8种方式
"""

import time
from selenium import webdriver

def find_elements():
    '''定位一组元素'''
    a = webdriver.Firefox()
    a.get('http://sahitest.com/demo/keypress.htm')
    a.maximize_window()
    b = a.find_elements_by_tag_name('input')#选择页面上所有tag name为input的元素
    for i in b:#然后从中过滤type为radio的元素
        if i.get_attribute('type') == 'radio':
            i.click()
            time.sleep(1)
    print(len('radio'))#打印当前页面上type为radio的个数

    a.find_elements_by_tag_name('input').pop(-2).click()#pop(-2)：获取倒数第二个元素，并点击
    '''
    pop()方法用于获取列表中的一个元素（默认为最后一个元素），并且返回该元素的值
    pop()或pop(-1)：默认获取一组元素中的最后一个
    pop(0))：默认获取一组元素中的第一个
    pop(1)：默认获取一组元素中的第2个
    '''

if __name__ == '__main__':
    find_elements()