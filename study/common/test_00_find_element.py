#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@others:     DTStudio, All rights reserved-- Created on 2016/11/09
@desc:       讲讲web项目中常用的方法属性
webdriver 提供了八种元素定位方法：
id、name、class name、tag name、link text、partial link text、xpath、css selector
在 Python 语言中对应的定位方法如下：
find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()
"""
from selenium import webdriver
import os
import time

path = os.getcwd()
path = 'file://' + path.split('test_case')[0] + 'demo_html' + os.sep + 'test.html'

test_html = path.decode('gbk').encode('utf-8')
baidu_url = 'http://www.baidu.com'

dr = webdriver.Firefox()
dr.implicitly_wait(30)
dr.get(baidu_url)

# 百度搜索框的html
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

# 1.根据id属性定位, id="kw"
dr.find_element_by_id('kw').clear()
dr.find_element_by_id('kw').send_keys('python')

# 2.根据name属性定位, name="wd"
dr.find_element_by_name('wd').clear()
dr.find_element_by_name('wd').send_keys('python')

# 3.根据class属性定位, class="s_ipt"
dr.find_element_by_class_name('s_ipt').clear()
dr.find_element_by_class_name('s_ipt').send_keys('python')

# 4.find_element_by_tag_name(), 搜索框的标签是<input></input>
# TIPS：通常很少使用tagname定位，因为页面上包含的相同标签数太多时，
# 比如_testfile页面，包含了3个input元素，使用find_element_by_tag_name('input')时，
# driver是无法区分出你到底要对哪个input操作，这里我们使用find_elements_by_tag_name('input')
# 注意这里find_elements_xxx的用法
dr.get(test_html)
eles = dr.find_elements_by_tag_name('input')
for e in eles:
    if e.get_attribute('id') == 'username':
        e.send_keys(u'这是用户名输入框')

# 5.find_element_by_link_text()
# <a onmousedown="return ns_c({'fm':'behs','tab':'tj_duty'})" href="http://www.baidu.com/duty/">使用百度前必读</a>
# 加 u 的作用是把中文字符串转换成unicode 编码
dr.get(baidu_url)
dr.find_element_by_link_text(u'使用百度前必读').click()

# 6.find_element_by_partial_link_text(), partial link text是对link text的补充。
# 只要取文本链接中的一部分即可，下面2行代码定位到的是同一个元素
dr.back()  # 返回上一页
dr.find_element_by_partial_link_text(u'使用百度').click()
dr.back()
dr.find_element_by_partial_link_text(u'百度前必读').click()

# 7.find_element_by_xpath()
dr.back()
# 7.1 使用绝对路径xpath定位
dr.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div/form/span[1]/input").send_keys('0')
# 7.2 使用相对路径的xpath定位
# 关于xpath的技巧，建议亲们在后期深入学习时重点研究下。通过常规方法不能定位元素时，使用xpath/css肯定是可行的。
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
dr.find_element_by_xpath("//input[@id='kw']").send_keys('1')
dr.find_element_by_xpath("//input[@name='wd']").send_keys('2')
dr.find_element_by_xpath("//input[@class='s_ipt']").send_keys('3')
dr.find_element_by_xpath("//*[@class='s_ipt']").send_keys('4')

# 8.find_element_by_css_selector()
dr.find_element_by_css_selector(".s_ipt").send_keys('5')  # .号后面跟的是class属性, class="s_ipt"
dr.find_element_by_css_selector("#kw").send_keys('6')  # #号后面跟的是id属性, id="kw"

# 这里停留30秒，方便大家看下效果，百度输入框里输入的是不是0123456
time.sleep(30)

#
print(u"搜索按钮的文字是>>>"), dr.find_element_by_id('su').text

dr.get(baidu_url)
news_link = dr.find_element_by_link_text(u"新闻")
print(u"新闻链接是>>>"), news_link.get_attribute("href")
print(u"新闻链接的name属性是>>>"), news_link.get_attribute("name")

# 9.退出，有2种方法
dr.quit()  # 关闭【所有窗口】，并退出相关的驱动程序，
# dr.close()    # 关闭【当前窗口】，注意两者的区别

# find_element_by_xxxx 和find_elements_by_xxx的区别：
# find_element_by_xxxx：定位一个元素
# find_elements_by_xxx：定位一组元素，得到的是一个list，要从list取值后再对每个元素做具体操作
