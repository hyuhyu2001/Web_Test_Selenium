#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     https://shop60459643.taobao.com
@contact:    no19@foxmail.com, https://shop60459643.taobao.com
@others:     DTStudio, All rights reserved-- Created on 2016/10/25
@desc:        send mail
"""
import unittest
import time
import xml.dom.minidom
import os
import sys
from selenium import webdriver

# 下面2行代码是为了方便每个脚本可以独立运行。
# 如果从all_test.py开始运行整个项目的test case时，将下面的代码放到all_test.py里面即可，不需要在每个py文件里都加上
cur_dir = os.getcwd()
sys.path.append(cur_dir.split(r'\test_case')[0])

from public_web import login



fo = os.path.dirname(__file__)  # os.getcwd()
fpath = fo.split('test_case')[0] + 'test_data' + os.sep + 'login.xml'
# 打开 xml 文档
dom = xml.dom.minidom.parse(fpath)

# 得到文档元素对象
root = dom.documentElement


class TestSendMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []

    # 只填写收件人发送邮件
    def test_send_mail(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self, "xxxx", "xxxx")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        # 填写收件人
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        # 发送邮件
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        # 断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text, u'发送成功')
        login.logout(self)

    # 填写收件人和、主题发送邮件
    def test_send_mail2(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self, "xxxx", "xxxx")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        # 填写收件人
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        # 添加主题
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and "
                                     "@type='text' and @maxlength='256']").send_keys(u'给小明的信')
        # 发送邮件
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        # driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        time.sleep(3)
        # 断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text, u'发送成功')
        login.logout(self)

    # 填写收件人、主题和附件发送邮件
    def test_send_mail3(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self, "xxx", "xxx")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and "
                                     "@type='text' and @maxlength='256']").send_keys(u'给小明的信')
        #上传附件
        driver.find_element_by_class_name("O0").send_keys('D:\\upfile.txt')
        #发送邮件
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        time.sleep(3)
        #断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text, u'发送成功')
        login.logout(self)

    # 填写收件人、主题和正文发送邮件
    def test_send_mail4(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self, "xxx", "xxx")
        #写信
        driver.find_element_by_css_selector("#_mail_component_47_47 > span.oz0").click()
        #填写收件人和主题
        driver.find_element_by_xpath("//*[@class='bz0']/div[2]/div/input").send_keys('testingwtb@126.com')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and "
                                     "@type='text' and @maxlength='256']").send_keys(u'给小明的信')
        #定位富文本表单
        class_name = driver.find_element_by_class_name('APP-editor-iframe')
        driver.switch_to.frame(class_name)
        #编写邮件正文
        driver.find_element_by_tag_name('body').send_keys(u'你好，小明好久不见。')
        #断言发送结果
        text = driver.find_element_by_class_name('tK1').text
        self.assertEqual(text, u'发送成功')
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
