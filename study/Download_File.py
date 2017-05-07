#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:下载文件
下面两种支持firefox和chrome的下载，同时也可以用autolt来下载
"""

from selenium import webdriver
from time import sleep

def firefox_download():
    '''火狐浏览器下载文件
    browser.download.dir：指定下载路径
    browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
    browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器，True为显示，False为不显示
    browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问'''
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'd:\\')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

    driver = webdriver.Firefox(firefox_profile=profile)

    driver.get('http://sahitest.com/demo/saveAs.htm')
    driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
    sleep(3)
    driver.quit()

def chrome_download():
    '''chrome浏览器下载文件
   download.default_directory：设置下载路径
    profile.default_content_settings.popups：设置为 0 禁止弹出窗口'''
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=options)
    driver.get('http://sahitest.com/demo/saveAs.htm')
    driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    firefox_download()