#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:元素操作，比如清除文本，模拟按键输入，单击元素
"""
from selenium import webdriver

def operation_element():
    '''元素操作有清除、输入、点击等操作
    报错：Message: Unable to locate element
    解决方法：你定位的用户名输入框元素节点上面有个iframe,所以要先进入找个iframe中，还有因为你的用户名和密码输入框元素ID是动态变化的，所以取ID会每次运行找不到元素，所以可以用name定位。
    如果你后面要定位的元素不在那个iframe下，需要跳出iframe,可以使用driver.switch_to_default_content()'''
    a = webdriver.Firefox()
    a.get('http://mail.163.com/')
    a.find_element_by_id("lbNormal").click() #进入一个iframe
    a.switch_to.frame("x-URS-iframe")
    b = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')#a.find_element_by_name("email")
    b.clear()#清除文本
    b.send_keys('username')#输入文字
    c = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]')#a.find_element_by_name("password")
    c.clear()#清除文本
    c.send_keys('password')#输入文字
    d = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a')#a.find_element_by_id('dologin')
    d.click()#点击按钮

def operation_element1():
    '''WebElement接口常用方法1：
    submit()方法用于提交表单，有时候submit()和click()方法可以互相换来使用'''
    a = webdriver.Firefox()
    a.get('http://www.youdao.com/')
    b = a.find_element_by_css_selector('html body div#search div.wrap form#form div#border input#translateContent')
    b.clear()
    b.send_keys('hello')
    c = a.find_element_by_css_selector('html body div#search div.wrap form#form button')
    c.submit() #submit()方法提交表单

def operation_element2():
    '''WebElement接口常用方法2：
    size：返回元素的尺寸
    text：获取元素的文本
    get_attribute(name)：获得属性值
    is_displayed()：获取该元素是否用户可见
    '''
    a = webdriver.Firefox()
    a.get('http://www.youdao.com/')
    b = a.find_element_by_css_selector('html body div#search div.wrap form#form div#border input#translateContent')
    print(b.size)#获得输入框的尺寸
    print(b.text)#获得输入框text的值
    print(b.get_attribute('type'))#获得type属性的值，同时可以是id、name或者其他属性
    print(b.is_displayed())#返回元素的接口是否可见
    b.clear()
    b.send_keys('hello')
    c = a.find_element_by_css_selector('html body div#search div.wrap form#form button')
    c.submit()

if __name__ == '__main__':
    operation_element()