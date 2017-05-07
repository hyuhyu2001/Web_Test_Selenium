#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:多窗口管理
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://www.baidu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'

def window_multi():
    '''多窗口操作
    句柄：句柄是整个windows的基础。一个句柄是指使用的唯一的整数值，即一个四字节长的数值，来标识应用程序中的不同对象和同类对象中的不同实例
        比如一个窗口、按钮、图标、滚动条、输出设备、控件或者文件等'''
    d = webdriver.Firefox()
    d.get(url)
    d.find_element_by_id('kw').clear()
    d.find_element_by_id('kw').send_keys('麦子学院')
    d.find_element_by_id('su').click()
    d.maximize_window()
    time.sleep(2)
    d.find_element_by_partial_link_text(r'麦子学院 - 专业IT职业教育平台').click()
    print(d.window_handles)#打印出目前所有的句柄，打开多个窗口时会有多个句柄，所有句柄存在window_handles的列表中
    print(d.current_window_handle)#打印出当前所在的句柄
    d.switch_to.window(d.window_handles[1])#移动句柄至列表下标为1的值
    print(d.current_window_handle)#打印出当前所在的句柄
    login_test(d)

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def login_test(d):
    #time.sleep(7)
    d.maximize_window()
    # d.find_element_by_link_text(login_text).click()
    ele_login = get_ele_times(d,10,lambda d:d.find_element_by_link_text(login_text))#调用延时的WebDriverWait
    ele_login.click()
    time.sleep(2)
    #d.find_element_by_id('login_close').click() #关闭窗口
    account_ele = d.find_element_by_id('id_account_l')
    time.sleep(2)
    account_ele.clear()
    account_ele.send_keys(account)
    pwd_ele = d.find_element_by_id('id_password_l')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    d.find_element_by_id('login_btn').click()

if __name__ == '__main__':
    window_multi()