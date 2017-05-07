#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:为了增加自动化的脚本稳定性，增加了元素等待，元素等待分为三种：
1、显式等待：使webdriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
    WebDriverWait(driver,timeout,poll_frequency,ignored_exceptions)
    说明：timeout为最长超时时间，默认以秒为单位；poll_frequency为检测的间隔（步长）时间，默认为0.5秒；
        ignored_exceptions为超时后的异常信息，默认情况下抛NoSuchElementException异常
    WebDriverWait()一般配合until()或者until_not()方法配合使用
        until(method,message='')：该方法提供的驱动程序作为一个参数，直到返回值为True
        until_not(method,message='')：该方法提供的驱动程序作为一个参数，直到返回值为False
2、隐式等待：如果某些元素不是立即可用的，隐式等待是告诉WebDriver去等待一定的时间后去查找元素。 默认等待时间是0秒，一旦设置该值，隐式等待是设置该WebDriver的实例的生命周期。
    driver.implicitly_wait(10)
3、sleep休眠：time模块下的sleep()方法，可以在脚本执行到某一位置时做固定时间的休眠，同时支持小数，比如sleep(0.5)
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #导入显式等待的模块
from selenium.webdriver.support import expected_conditions as EC #expected_conditions提供预期条件判断的方法
from selenium.common.exceptions import NoSuchElementException
from time import ctime

def wait_element():
    '''显式等待'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    ele = WebDriverWait(a,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))#写法一：判断元素是都加在了bom树中
    # ele = WebDriverWait(a,5,0.5).until(lambda a:a.find_element_by_id('kw'))#写法2：通过lambda匿名函数
    # def get(ele,times,func):
    #     return WebDriverWait(driver,times).until(func) #写法3：通过公共函数
    ele.send_keys('selenium')

def wait_element1():
    '''隐式等待'''
    a = webdriver.Firefox()
    a.implicitly_wait(10)
    a.get('https://www.baidu.com/')

    try:
        print(ctime())
        a.find_element_by_id('kw22').send_keys('selenium')
    except NoSuchElementException as e:
        print(e)
    finally:
        print(ctime())
        a.quit()

if __name__ == '__main__':
    wait_element1()


