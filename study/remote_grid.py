#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

from selenium.webdriver import Remote

def main(driver):
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys('selenium2')
    driver.find_element_by_id('su').click()

def remote_ts():
    '''简单示例'''
    driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities={
                        "browserName": "firefox",
                        "version": "42.0",
                        "platform": "ANY",
                        "javascriptEnabled": True,
                    }
                    )
    return driver

def remote_ts2():
    '''修改脚本使其在不同的节点及浏览器上运行'''
    lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
             'http://127.0.0.1:5555/wd/hub': 'firefox',
             'http://10.16.6.166:6666/wd/hub': 'internet explorer'}
    for host,browser in lists.items():
        print(host,browser)
        driver = Remote(command_executor=host,
                        desired_capabilities={
                            "browserName": browser,
                            "version": "42.0",
                            "platform": "ANY",
                            "javascriptEnabled": True,
                        }
                        )
    return driver

if __name__ == '__main__':
    driver = remote_ts()
    main(driver)