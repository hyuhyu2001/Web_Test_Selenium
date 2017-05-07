#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:input上传文件
示例网址：http://www.sahitest.com/demo/php/fileUpload.htm
webdriver是无法操作windows控件的，所以对于初学者来说，一般思路会卡在如何识别window控件上。
web页面上传有两种方式：
（1）普通上传：普通的附件上传是将本地的路径作为一个值放在input标签中，通过form表单将这个值提交到服务器
（2）插件上传：一般是指基于Flash、JavaScript或Ajax等技术等事项的上传功能
"""
from selenium import webdriver
import os,time

def upload_file_input():
    '''input标签时可以直接send_keys的，send_keys实现上传'''
    driver = webdriver.Firefox()
    driver.get(r'http://www.sahitest.com/demo/php/fileUpload.htm')
    time.sleep(2)

    #定位上传按钮，添加本地文件,绝对路径
    upload = driver.find_element_by_id('file')
    upload.send_keys(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\test.txt')
    print(upload.get_attribute('value'))

    #相对路径
    # driver.find_element_by_name('file').send_keys('D:\\\study\\test.txt')

'''
非input上传文件：
 1.autoIT，借助外力，我们去调用其生成的au3或exe文件
    autolt是用例进行windows GUI的自动化测试，她利用模拟键盘按键、鼠标移动和窗口/控件的组合来实现自动化任务
    （1）autolt windows info：用于识别windows控件信息
    （2）compile script to.exe：用于将Autolt生成exe执行文件
    （3）run scipt：用于执行autolt脚本
    （4）sciTe script editor：用于编写autolt脚本
 2.Python pywin32库，识别对话框句柄，进而操作：需要工具：Spy++，pywin32的库
 3.SendKeys库:首先要安装SendKeys库，可以用pip安装  pip install SendKeys
 4.keybd_event，跟3类似，不过是模拟按键，ctrl+a，ctrl+c， ctrl+v…;win32api提供了一个keybd_event()方法模拟按键，不过此方法比较麻烦，也不稳定，所以很不推荐
'''
def upload_file_NoInput_Autolt():
    '''非input标签时，方法1：Autolt上传
    http://www.cnblogs.com/fnng/p/4188162.html'''
    driver = webdriver.Firefox()

    # 打开上传功能页面
    file_path = 'file:///' + os.path.abspath('upfile.html')
    driver.get(file_path)

    # 点击打开上传窗口
    driver.find_element_by_name("file").click()
    # 调用upfile.exe上传程序。python调用exe程序并在python的可控范围内，exe执行多长时间，执行是否出错，python程序都无法得知。
    os.system("D:\\upfile.exe")

    driver.quit()

if __name__=='__main__':
    upload_file_input()
    # file_path = 'file:///'+os.path.abspath('upfile.html')
    # print(os.path.abspath('upfile.html'))
    # print(file_path)