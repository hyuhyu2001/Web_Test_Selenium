#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
一、测试脚本模块化之后，实现数据与脚本的分离
1、将代码中的数据剥离，设计合理的数据结构
2、设计数据读取模块，从文件中读取测试数据
3、数据设计：字典形式，设计字典的key和value
二、进行错误处理的优化
1、测试结果（包含错误元素信息）保存到数据文件
2、修改代码、支持错误处理
"""

import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
from study.DataSeparation import usedata
from study.DataSeparation import log_module

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    d = webdriver.Firefox()
    time.sleep(2)
    return d

def openURL(d,url):
    d.get(url)
    d.maximize_window()

def find_Element(d,**ele_dict):
    if 'text_id' in ele_dict:
        ele_login = get_ele_times(d,10,lambda d:d.find_element_by_link_text(ele_dict.get('text_id')))
        ele_login.click()
    useEle = get_ele_times(d,2,lambda d:d.find_element_by_id(ele_dict.get('userid')))
    pwdEle = get_ele_times(d,2,lambda d:d.find_element_by_id(ele_dict.get('pwdid')))
    loginEle = get_ele_times(d,2,lambda d:d.find_element_by_id(ele_dict.get('loginid')))
    return useEle,pwdEle,loginEle

def sendVals(arg,*ele_tuple):
    '''eletuple:account:uname,pwd'''
    listkey=['uname','pwd']
    i = 0
    for key in listkey:
        time.sleep(2)
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg.get(key))
        i+=1
    ele_tuple[2].click()

def checkResult(d,arg,log,**ele_dict):
    # err = d.find_element_by_id(err_id)
    # if err.text.isspace() is False:#判断是否全是空白字符，并至少有一个字符
    # if d.current_url == r'http://www.maiziedu.com':通过current_url和title也无法判断，因为值一样
    time.sleep(1)
    try:
        get_ele_times(d, 5, lambda d: d.find_element_by_link_text(ele_dict.get('logout')))#通过退出元素是否查找到确认是否登录成功
        print('Account And Pwd Right!')
        msg = 'uname(%s) pwd(%s):pass\n'%(arg.get('uname'),arg.get('pwd'))
        log.log_write(msg) #增加写入日志
        result = True
    except Exception as e:
        print('Account And Pwd Error!')
        err = d.find_element_by_id(ele_dict.get('errorid'))
        msg = 'uname(%s) pwd(%s):error:%s\n'%(arg.get('uname'),arg.get('pwd'),err.text)
        log.log_write(msg)
        result = False
    return result

def logout(d,**ele_dict):
    # a = d.find_element_by_xpath(r'/html/body/div[2]/div/div').click()
    # ActionChains(d).move_to_element(logout).perform() 不是悬浮的
    get_ele_times(d, 5, lambda d: d.find_element_by_link_text(ele_dict.get('logout'))).click()
    time.sleep(2)

def login_maizi(*user_list,**ele_dict):
    d = openBrower()
    openURL(d,ele_dict['url'])
    log = log_module.Logiofo()

    ele_tuple = find_Element(d,**ele_dict)
    for arg in user_list:
        sendVals(arg,*ele_tuple)
        result = checkResult(d,arg,log,**ele_dict)
        if result == True:
            logout(d,**ele_dict)#登出
            ele_tuple = find_Element(d,**ele_dict)#登入
    log.log_close()

if __name__ == '__main__':
    # url = 'http://www.maiziedu.com/'
    # login_text = '登录'
    # account = 'maizi_test@139.com'
    # pwd = 'abc123456'
    # ele_dict = {'url':url,'text_id':login_text,'userid':'id_account_l',\
    #             'pwdid':'id_password_l','loginid':'login_btn',\
    #             'errorid':'该账号格式不正确'}errorid=login-form-tips
    # user_list = [{'uname':account,'pwd':pwd}]
    ele_dict = usedata.get_webinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\webinfo.txt')
    user_list = usedata.get_userinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\userinfo.txt')
    login_maizi(*user_list,**ele_dict)