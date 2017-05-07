#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:鼠标事件：鼠标交互方式：比如鼠标右击、双击、悬停、甚至是鼠标拖动等功能，这些鼠标操作都封装在ActionChains类提供
点击操作：http://sahitest.com/demo/clicks.htm
鼠标移动：http://sahitest.com/demo/mouseover.htm
拖拽网页：http://sahitest.com/demo/dragDropMooTools.htm
按键1：http://sahitest.com/demo/keypress.htm
按键2：http://sahitest.com/demo/label.htm
"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def chains_action1():
    '''鼠标右键操作'''
    a = webdriver.Firefox()
    # a = webdriver.Chrome()
    a.get('https://www.baidu.com/')
    a.maximize_window()
    b = a.find_element_by_xpath("//div[@id='lg']/img") #定位到百度图片
    ActionChains(a).context_click(b).perform() #对图片进行右键操作【问题：右键之后如何继续操作？】
    time.sleep(3)
    b.sendkeys(Keys.DOWN)#按下键，进入右键菜单第一个选项
    b.send_keys(Keys.ENTER)#b.click()

def chains_action2():
    '''鼠标悬停操作'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_link_text("设置") #定位到设置按钮
    ActionChains(a).move_to_element(b).perform()#鼠标悬停在设置按钮上
    c =a.find_element_by_link_text('搜索设置') #悬停后对下来按钮进行点击操作
    c.click()

def chains_action3():
    '''鼠标双击操作'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    b = a.find_element_by_link_text("地图")
    ActionChains(a).double_click(b).perform()#鼠标双击进行操作

def chains_action4():
    '''鼠标拖拽操作'''
    driver = webdriver.Firefox()
    driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
    dragger = driver.find_element_by_id('dragger')  # 被拖拽元素
    item1 = driver.find_element_by_xpath('//div[text()="Item 1"]')  # 目标元素1
    item2 = driver.find_element_by_xpath('//div[text()="Item 2"]')  # 目标2
    item3 = driver.find_element_by_xpath('//div[text()="Item 3"]')  # 目标3
    item4 = driver.find_element_by_xpath('//div[text()="Item 4"]')  # 目标4

    action = ActionChains(driver)
    action.drag_and_drop(dragger, item1).perform()  # 1.移动dragger到目标1
    time.sleep(2)
    action.click_and_hold(dragger).release(item2).perform()  # 2.效果与上句相同，也能起到移动效果
    time.sleep(2)
    action.click_and_hold(dragger).move_to_element(item3).release().perform()  # 3.效果与上两句相同，也能起到移动的效果
    time.sleep(2)
    # action.drag_and_drop_by_offset(dragger, 400, 150).perform() # 4.移动到指定坐标
    action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()  # 5.与上一句相同，移动到指定坐标
    time.sleep(2)

def chains_action5():
    '''鼠标单击、双击、右键操作的链式用法'''
    driver = webdriver.Firefox()
    driver.get('http://sahitest.com/demo/clicks.htm')
    driver.maximize_window()
    click_btn = driver.find_element_by_xpath('//input[@value="click me"]')#单击
    double_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')#双击
    right_btn = driver.find_element_by_xpath('//input[@value="right click me"]')#右键单击

    ActionChains(driver).click(click_btn).double_click(double_btn).context_click(right_btn).perform()#链式用法
    print(driver.find_element_by_name('t2').get_attribute('value'))

def chains_action6():
    '''按键操作1'''
    driver = webdriver.Firefox()
    driver.get('http://sahitest.com/demo/keypress.htm')
    driver.maximize_window()

    input1 = driver.find_element_by_xpath('/html/body/form/input[1]')
    input2 = driver.find_element_by_xpath('/html/body/form/input[2]')

    action = ActionChains(driver)
    input1.click()
    action.send_keys('Test keys').perform()
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()#ctrl+a
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()#ctrl+c
    action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform() # ctrl+v

def chains_action7():
    '''按键操作2'''
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/keypress.htm')

    key_up_radio = driver.find_element_by_id('r1')  # 监测按键升起
    key_down_radio = driver.find_element_by_id('r2')  # 监测按键按下
    key_press_radio = driver.find_element_by_id('r3')  # 监测按键按下升起

    enter = driver.find_elements_by_xpath('//form[@name="f1"]/input')[1]  # 输入框
    result = driver.find_elements_by_xpath('//form[@name="f1"]/input')[0]  # 监测结果

    # 监测key_down
    key_down_radio.click()
    ActionChains(driver).key_down(Keys.CONTROL, enter).key_up(Keys.CONTROL).perform()
    print(result.get_attribute('value'))

    # 监测key_up
    key_up_radio.click()
    enter.click()
    ActionChains(driver).key_down(Keys.SHIFT).key_up(Keys.SHIFT).perform()
    print(result.get_attribute('value'))

    # 监测key_press
    key_press_radio.click()
    enter.click()
    ActionChains(driver).send_keys('a').perform()
    print(result.get_attribute('value'))

def chains_action8():
    '''按键操作3'''
    a = webdriver.Firefox()
    a.get('https://www.baidu.com/')
    a.maximize_window()
    b = a.find_element_by_css_selector('form.fm>span>input.s_ipt')
    b.send_keys('selenium1')
    b.send_keys(Keys.BACKSPACE)
    b.send_keys(Keys.SPACE)
    b.send_keys("教程")
    b.send_keys(Keys.CONTROL,'a')
    b.send_keys(Keys.CONTROL,'x')
    b.send_keys(Keys.CONTROL,'v')
    a.find_element_by_id('su').send_keys(Keys.ENTER) #回车键代替单击操作

if __name__ == '__main__':
    chains_action8()