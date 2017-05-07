#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:操作cookie
1、需要验证浏览器中的cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的
webdriver提供了操作cookie的方法，可以读取、添加和删除cookie的信息
2、什么情况下用到cookie，比如用户登陆时，会将用户的用户名写入浏览器cookie，指定的key为“username”，我们就可以通过get_cookies()找到username，打印value
如果找不到username或对应的value为空，那么说明cookie没有成功的保存到浏览器中。
webdriver操作cookie的方法
"""

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

#获得cookie信息,返回所有cookie信息，cookie是以字典的形式进行存放的
cookie = driver.get_cookies()
print(cookie)
print(driver.get_cookie('YOUDAO_MOBILE_ACCESS_TYPE'))#返回字典的key为“name”的cookie信息

driver.add_cookie({'name':'key-aaaaa','value':'value-bbbb'})#向cookie的name和value中添加会话信息


driver.delete_cookie('key-aaaaa')#删除指定name的cookie信息
# driver.delete_all_cookies()#删除所有cookie信息

for cookie in driver.get_cookies():#遍历cookies中的name和value信息并打印
    print("%s>>%s"%(cookie['name'],cookie['value']))