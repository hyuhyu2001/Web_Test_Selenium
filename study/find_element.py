#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:WebDriver Api 从定位元素开始，包含8种元素定位方式
"""
from selenium import webdriver

def id_find_element():
    '''html规定id属性在HTML文档中必须是唯一的，类似于身份证号'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    print(a.title) #打印网页标题
    print(a.current_url) #打印网页URL
    b = a.find_element_by_id('kw') #通过ID定位元素
    b.send_keys('selenium')#输入输入值
    b.clear() #清空输入值
    b.send_keys('selenium2')
    c = a.find_element_by_id('su')  #通过ID定位元素
    c.click() #点击按钮
    a.back() #后退至上个网页
    a.quit()#退出并关闭浏览器及相关的驱动程序
    # id(b)
    # type(b)

def name_find_element():
    '''name类似于人名，name是属性值，在当前页面不唯一，不建议使用'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_name('wd') #通过name定位元素
    b.send_keys('selenium')
    c = a.find_element_by_id('su')
    c.click()
    a.quit()

def class_find_element():
    '''HTML规定class来指定元素的类型,执行会报错，不能保证唯一性'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_class_name('s_ipt') #通过class定位元素
    b.send_keys('selenium')
    c = a.find_element_by_class_name('bg s_btn btnhover')#通过class定位元素
    c.click()
    a.quit()

def tag_find_element():
    '''每个元素本质上也是一个tag，因为一个tag往往来定义一类功能，因为一个页面会有<div>、<input>等大量的tag，很难通过tag name去区分不同的元素'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_tag_name('input') #通过tag定位元素
    b.send_keys('selenium')
    a.quit()

def link_find_element():
    '''link定位主要专门用来定位文本连接，比如百度首页的新闻、hao123，主要通过元素标签对之间的文本信息来定位元素'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_link_text('新闻') #通过link定位元素
    b.click()
    a.back()
    c = a.find_element_by_link_text('hao123') #通过link定位元素
    c.click()
    a.quit()

def partial_link_find_element():
    '''因为id和name不一定会有，或者每一次刷新页面，id值都会随机变化，所以我们后面会用xpath和css定位'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    a.maximize_window() #最大化窗口
    c = a.find_element_by_partial_link_text('新') #通过partial link定位元素
    c.click()
    a.quit()

def xpath_find_element1():
    '''xpath是一种在XML文档中定位元素的语言，xpath用于在XML文档中通过元素和属性进行导航
    xpath节点类型：元素、属性、文本、命名空间、指令处理、注释及文档
    1、根据绝对路径去寻找xpath'''
    a = webdriver.Firefox()
    a.get(r'file:///D:/python_pycharmWorkspace/python36/Web_Test_Selenium/study/xpath.html')
    b = a.find_element_by_xpath('/html') #通过xpath定位:选取根基点的html
    print(b.text)
    c = a.find_element_by_xpath('/html/body/form/input') #通过xpath定位：根据绝对路径选择元素(通过xpath的一级级路径去确定元素，选择第一个)
    print(c.get_attribute('type')) #打印出对应元素的类型
    print(c.get_attribute('name'))#打印出对应元素的name
    d = a.find_element_by_xpath('/html/body/form/input[1]') #通过xpath定位：根据绝对路径选择元素,定位form下第1个出现input的元素
    print(d.get_attribute('name'))
    e = a.find_element_by_xpath('/html/body/form/input[2]') #通过xpath定位：根据绝对路径选择元素,定位form下第2个出现input的元素
    print(e.get_attribute('name'))
    f = a.find_element_by_xpath('/html/body/p/input') #通过xpath定位：根据绝对路径选择元素,定位p下第1个出现input的元素
    print(f.get_attribute('name'))
    a.quit()

def xpath_find_element2():
    '''2、根据整个文档扫描去寻找xpath,//xxx；父元素等'''
    a = webdriver.Firefox()
    a.get(r'file:///D:/python_pycharmWorkspace/python36/Web_Test_Selenium/study/xpath.html')
    b = a.find_element_by_xpath('//input') #通过xpath定位:在全文搜索中找到第1个input的元素
    print(b.get_attribute('type')) #打印出对应元素的类型
    print(b.get_attribute('name'))#打印出对应元素的name
    c = a.find_element_by_xpath('//input[2]') #找到第2个input的元素，找第3个时会报错，因为找到后只查询同一目录结构下的，不在找上一级以及其他同级。
    print(c.get_attribute('type'))
    print(c.get_attribute('name'))
    d = a.find_element_by_xpath('//p/input') #找到父元素e为p的input节点
    print(d.get_attribute('name'))
    e = a.find_element_by_xpath('//p/input/.') #选取当前节点的父元素节点
    print(e.tag_name)
    print(e.get_attribute('type'))
    print(e.get_attribute('name'))
    f = a.find_element_by_xpath('//p/input/..') #选取父元素地址
    print(f.tag_name)
    a.quit()

def xpath_find_element3():
    '''3、利用元素属性定位：//xxx[@id] 与 //xxx[@id=yyy] 的用法；count的方法'''
    a = webdriver.Firefox()
    a.get(r'file:///D:/python_pycharmWorkspace/python36/Web_Test_Selenium/study/xpath.html')
    b = a.find_element_by_xpath('//input[@id]') #全文找出input元素，且含有id的
    print(b.get_attribute('type'))
    print(b.get_attribute('name'))
    c = a.find_element_by_xpath('//input[not(@id)]') #全文找出input元素，第一个不含有id的
    print(c.get_attribute('type'))
    print(c.get_attribute('name'))
    d = a.find_element_by_xpath('//input[@id ="test"]') #全文找出input元素，且id = 'test'的,也可以通过name定位比如'//input[@name ="lastname"]'
    print(d.get_attribute('type'))
    print(d.get_attribute('name'))
    e = a.find_element_by_xpath('//*')#全文搜索，*代表不想指定标签名
    print(e.tag_name)
    f = a.find_element_by_xpath('//*[count(input)=2]')#全文搜索,且input只出现2次的
    print(f.tag_name)
    g = a.find_element_by_xpath('//*[count(input)=1]')#全文搜索,且input只出现1次的
    print(g.tag_name)
    a.quit()

def xpath_find_element4():
    '''4、local-name()等方法的使用'''
    a = webdriver.Firefox()
    a.get(r'file:///D:/python_pycharmWorkspace/python36/Web_Test_Selenium/study/xpath.html')
    b = a.find_element_by_xpath('//*[local-name()= "input"]') #全文找出元素名称=input的
    print(b.get_attribute('name'))
    c = a.find_element_by_xpath('//*[starts-with(local-name(),"in")]') #全文找出元素名称首先是以in开头的
    print(c.get_attribute('name'))
    d = a.find_element_by_xpath('//*[contains(local-name(),"i")]') #全文找出元素名称，包含i的，第一个出现的
    print(d.tag_name)
    e = a.find_element_by_xpath('//*[contains(local-name(),"i")][last()]') #全文找出元素名称，包含i的，最后一个出现的元素,也是会找相同级别的，不会往上级找
    print(e.tag_name)
    f = a.find_element_by_xpath('//form//*[contains(local-name(),"i")][last()]') #找form下找出元素名称，包含i的，最后1个出现的元素
    print(f.get_attribute('name'))
    g = a.find_element_by_xpath('//form//*[contains(local-name(),"i")][last()-1]') #找form下找出元素名称，包含i的，倒数第2个出现的元素
    print(g.get_attribute('name'))
    h = a.find_element_by_xpath('//form//*[string-length(local-name())=5]') #找form下,元素长度为5的元素
    print(h.tag_name)
    a.quit()


def xpath_find_element5():
    '''5、//xxx | //yyy 多个路径查找'''
    a = webdriver.Firefox()
    a.get(r'file:///D:/python_pycharmWorkspace/python36/Web_Test_Selenium/study/xpath.html')
    b = a.find_element_by_xpath('//title | //input') #全文title或者input的元素
    print(b.tag_name)
    a.quit()

def xpath_find_element6():
    '''6、使用逻辑运算法：如果一个属性不能唯一的区分一个元素，我们还可以使用逻辑运算符来连接多个属性来查找元素，比如and'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]') #全文找出元素名称=input的
    b.send_keys('selenium')
    c = a.find_element_by_id('su')
    c.click()

def css_find_element():
    '''CSS（Cascading Style Sheets）是一种语言，用来描述HTML和XML文档的表现。CSS使用选择器来为页面元素绑定属性
    CSS可以较为灵活的选择控件的任意属性，一般情况下定位也比xpath快'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_css_selector('html body div#wrapper div#head div.head_wrapper div.s_form div.s_form_wrapper.soutu-env-nomac.soutu-env-index form#form.fm span.bg.s_ipt_wr.quickdelete-wrap input#kw.s_ipt') #通过css定位元素
    b.send_keys('selenium')
    c = a.find_element_by_class_name('html body div#wrapper div#head div.head_wrapper div.s_form div.s_form_wrapper.soutu-env-nomac.soutu-env-index form#form.fm span.bg.s_btn_wr input#su.bg.s_btn')#通过css定位元素
    c.click()
    a.quit()

def css_find_element1():
    '''1、CSS属性定位的写法'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_css_selector('.s_ipt') #class属性定位，通过（.）表示通过class属性来定位元素，class='.s_ipt'的元素
    b.send_keys('selenium')
    c = a.find_element_by_css_selector('#su')#id属性定位，通过（#）表示通过id属性来定位元素，比如id='su'的元素
    c.click()
    a.quit()

def css_find_element2():
    '''2、CSS属性定位的写法'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    # b = a.find_element_by_css_selector('form#form>span>input#kw') #组合定位 （>）表示父子关系定位,找到form和input，且同时满足id值的条件
    b = a.find_element_by_css_selector('form.fm>span>input.s_ipt') #组合定位 （>）表示父子关系定位,找到form和input，且同时满足class值的条件
    b.send_keys('selenium')
    c = a.find_element_by_css_selector('[id="su"]')#通过属性定位及属性值
    c.click()
    a.quit()

if __name__ == '__main__':
    css_find_element2()
