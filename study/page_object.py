#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:page objcet模式
"""
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pip._vendor.distlib.locators import Page
from selenium.webdriver.support.ui import Select  # 导入下拉框函数
import unittest

class Page(object):
    #基础类，用于页面对象类的继承
    login_url = 'http://qf-uatqapp-w2/ProductApplication/Application'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.driver.maximize_window()

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url
        self.driver.get(url)
        self.driver.maximize_window()
        # assert self.on_page(), 'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def switch_frame(self, loc):
        return self.driver.switch_to_frame()


class LoginPage(Page):
    #页面对象的操作类
    url = '/'
    username_loc = (By.ID, "Account")
    password_loc = (By.ID, "Pwd")
    submit_loc = (By.ID, "Log_Submit")

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


class ProductPage(Page):
    customername_loc = (By.ID, "customerName")
    customerID_loc = (By.ID, "customerIDCard")
    applyCity_loc = (By.ID, "applyCity")

    # productCode_loc = (By.ID,"//option[@value='productCodesyd-6-24']")
    # productCode_value = (By.XPATH,"//option[@value='BYQSF0000']")
    # platform_loc = (By.ID,"platform")
    # platform_value = (By.XPATH,"//option[@value='BYQSF0000']")

    def type_customername(self, customername):
        self.find_element(*self.customername_loc).send_keys(customername)

    def type_customerID(self, customerId):
        self.find_element(*self.customerID_loc).send_keys(customerId)

    def type_applyCity(self, applyCityvalue):
        Select(self.find_element(*self.applyCity_loc)).select_by_value(applyCityvalue)  # 下拉框函数


def test_user_login(driver, username, password):
    page = LoginPage(driver)
    page.open()
    page.type_username(username)
    page.type_password(password)
    page.submit()

def test_apply_product(driver, customername, customerID, applyCityvalue):
    page1 = ProductPage(driver)
    page1.type_customername(customername)
    page1.type_customerID(customerID)
    page1.type_applyCity(applyCityvalue)


def main():
    driver = webdriver.Firefox()
    username = 'jiahua'
    password = 'Quarkhj05'
    customername = u'huajia'
    customerId = '310104198408020057'
    applyCityvalue = '025,025'
    test_user_login(driver, username, password)
    driver.implicitly_wait(30)
    test_apply_product(driver, customername, customerId, applyCityvalue)


if __name__ == '__main__':
    main()
    unittest.main()
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/30
@desc:       PageObject设计模式示例
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    基类，用于所有页面的继承
    """
    homepage = 'http://www.126.com'

    def __init__(self, selenium_driver, base_url=homepage, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        print(self.driver.current_url == (self.base_url + self.url))
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('%s page does not have "%s" locator' % (self, loc))


# 继承自Page这个类
class LoginPage(Page):
    """
        登录页面模型
    """
    url = '/'
    # 定位器
    username_loc = (By.ID, "idInput")
    password_loc = (By.ID, "pwdInput")
    submit_loc = (By.ID, "loginBtn")

    #Action
    def open(self):
        self._open(self.url)

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    """
    测试获取的用户名密码 是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    sleep(3)
    assert (username == 'xxxx@126.com'), u"用户名称不匹配，登录失败!"


def main():
    try:
        # Selenium
        driver = webdriver.Firefox()
        username = 'xxxx'
        password = 'xxx'
        test_user_login(driver, username, password)
    finally:
        # 关闭浏览器窗口
        driver.close()


if __name__ == '__main__':
    main()