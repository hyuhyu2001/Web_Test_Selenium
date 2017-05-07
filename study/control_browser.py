#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:控制浏览器的方法，比如控制浏览器的大小、操作浏览器的前进和后退
"""

from selenium import webdriver

def broswer_control1():
    '''控制浏览器的大小,set_window_size(480,800)和maximize_window() 实现'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    a.set_window_size(480,800)#设置浏览器宽480，高800显示
    # a.maximize_window() #最大化窗口
    b = a.find_element_by_css_selector('form.fm>span>input.s_ipt')
    b.send_keys('selenium')
    c = a.find_element_by_css_selector('[id="su"]')#通过属性定位及属性值
    c.click()
    a.quit()

def broswer_control2():
    '''控制浏览器的后退、前进，back()后退，forward()前进'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    a.get('http://news.baidu.com/') #访问新闻页面
    a.back()#后退
    a.forward()#前进

def broswer_control3():
    '''模拟浏览器刷新，有时需要F5刷新页面，通过refresh()实现'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    a.refresh()#刷新

if __name__ == '__main__':
    broswer_control3()