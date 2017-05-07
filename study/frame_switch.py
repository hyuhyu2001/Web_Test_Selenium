#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:多表单切换
"""

from selenium import webdriver

def operation_element():
    '''WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。
    这时需要通过switch_to.frame()方法将当前定位的主题切换到frame/iframe表单的内嵌页面中。
    '''
    a = webdriver.Firefox()
    a.get('http://mail.163.com/')
    a.find_element_by_id("lbNormal").click() #进入一个iframe
    a.switch_to.frame("x-URS-iframe") #将主体切换到frame表单的内嵌页面中
    b = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')#a.find_element_by_name("email")
    b.clear()
    b.send_keys('username')
    c = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]')#a.find_element_by_name("password")
    c.clear()
    c.send_keys('password')
    d = a.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a')#a.find_element_by_id('dologin')
    d.click()#点击按钮
    a.switch_to.parent_frame() #跳出当前一级表单
    # a.switch_to.default_content() #有多级表单的情况下，可以通过switch_to.default_content()跳回最外层的页面
    a.find_element_by_link_text('邮箱黄页').click()

'''
switch_to.frame()默认可以直接取表单的id和name属性，如果iframe没有可用的id和name属性，可以通过以下方式定位

#先通过xpath定位iframe
a = webdriver.Firefox()
a.get('http://mail.163.com/')
xf = a.find_element_by_id("lbNormal")#可以是xpath，css各种定位方式
#再将定位对象传给switch_to.frame()方法
a.switch_to.frame(xf)
'''
if __name__ == '__main__':
    operation_element()