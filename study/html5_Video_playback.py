#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:处理html5的视频播放
webdriver支持在指定的浏览器上测试html5，另外可以使用javascipt来测试这些功能
HTML5定义了一个新的元素<vidio>，指定了一个标准的方式来嵌入电影片段
这一章学习如何自动化测试<vidio>
javascript函数有个内置的对象叫做arguments，argument对象包含了函数调用的参数数组
currerntSrc属性返回当前音频/视频的URL，如果未设置音频/视频，则返回空字符串。
load(),play(),pause()等控制着视频的加载、播放和暂停
"""

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://videojs.com')
time.sleep(30)
video = driver.find_element_by_xpath("html/body/section[1]/div[1]/video")

#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print('start')
driver.execute_script("return arguments[0].play()",video)

#播放15秒
time.sleep(15)

#暂停视频
print('stop')
driver.execute_script("return arguments[0].pause()",video)

