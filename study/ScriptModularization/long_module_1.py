#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:测试脚本模块化
1、OpenBrowser
2、OpenURL
3、FindElement
4、SendKeys
5、CheckResult
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    d = webdriver.Firefox()
    time.sleep(2)
    d.maximize_window()
    return d

def openUrl(d,url):
    d.get(url)

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
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(arg.get(key))
        i+=1
    ele_tuple[2].click()

def checkResult(d,text):
    try:
        err = d.find_element_by_id(text)
        print('Account And Pwd Error!')
        print(err.text)
    except:
        print('Account And Pwd Right!')

def login_maizi(*user_list,**ele_dict):
    d = openBrower()
    openUrl(d,ele_dict['url'])

    ele_tuple = find_Element(d,**ele_dict)
    for arg in user_list:
        sendVals(arg,*ele_tuple)
        checkResult(d,ele_dict.get('login-form-tips'))

if __name__ == '__main__':
    url = 'http://www.maiziedu.com/'
    login_text = '登录'
    account = 'maizi_test@139.com'
    pwd = 'abc123456'
    ele_dict = {'url':url,'text_id':login_text,'userid':'id_account_l',\
                'pwdid':'id_password_l','loginid':'login_btn',\
                'login-form-tips':'该账号格式不正确'}
    user_list = [{'uname':account,'pwd':pwd}]

    login_maizi(*user_list,**ele_dict)