#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:excel：读取文件里的数据,生成web_info 和 user_list
"""
import xlrd

def get_webinfo(path):
    web_info = {}
    with open(path,'r') as f:
        for line in f:
            result = line.strip().split('=')#第二种下发result = [ele.strip() for ele in line.split('=')]
            web_info.update(dict([result]))
    return web_info

def get_userinfo(path):
    user_info = []
    with open(path,'r') as f:
        for line in f:
            user_dict = {}
            result = [ele.strip(';\n') for ele in line.split(',')]
            for r in result:
                account = r.strip().split('=')
                user_dict.update(dict([account]))
            user_info.append(user_dict)
    return user_info

class XLUserInfo(object):
    def __init__(self,path = ''):
        self.xl = xlrd.open_workbook(path)

    def get_sheet_info(self):
        listkey=['uname','pwd']
        infolist = []
        infodict = {}
        for row in range(1,self.sheet.nrows):#从1开始循环
            info = self.sheet.row_values(row)
            infodict.update(dict([info]))
            tmp = zip(listkey,info)
            infolist.append(dict(tmp))
        return {'infodict':infodict,'infolist':infolist}

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self,index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

if __name__ == '__main__':
    # info = get_webinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\webinfo.txt')
    # for key in info:
    #     print(key,info[key])
    # info = get_userinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\userinfo.txt')
    userlinfo = XLUserInfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparationExcel\userinfo.xlsx')
    # info = xlinfo.get_sheetinfo_by_index(0)
    info = userlinfo.get_sheetinfo_by_name('Sheet1') #Sheet1必须区分大小写
    print(info)
    weblinfo = XLUserInfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparationExcel\webinfo.xlsx')
    winfo = weblinfo.get_sheetinfo_by_name('Sheet1') #Sheet1必须区分大小写
    print(winfo)
