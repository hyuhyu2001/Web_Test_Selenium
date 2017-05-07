#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:增加日志输出，excel
测试结果（包含错误元素信息）保存到数据文件
log_write(self,msg)：写日志
log_close(self)：关闭日志文件
"""

import time
import xlsxwriter

class Logiofo(object):
    def __init__(self,path='',mode='w'):
        fname =  path + time.strftime('%Y-%m-%d',time.gmtime())
        self.log = open(path + fname + '.txt',mode)

    def log_init(self,sheetname,*title):
        pass

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()


class XLLogiofo(object):
    def __init__(self, path='', mode='w'):
        fname = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(path+fname+'.xls')
        self.style = self.xl.add_format({'bg_color':'red'})

    def xl_write(self, *args):
        col = 0
        style = ''
        if  'Error' in args:
            style = self.style
        for val in args:
            self.sheet.write(self.row,col,val,style)
            col+=1
        self.row+=1

    def log_init(self, sheetname,*title):
        self.sheet = self.xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E',30)
        self.xl_write(*title)

    def log_write(self,*args):
        self.xl_write(*args)

    def log_close(self):
        self.xl.close()


if __name__ == '__main__':
    # log = Logiofo()
    # log.log_write('test Loginfo 测试')
    # log.log_close()
    loginfo = XLLogiofo()
    loginfo.log_init('test','uname','pwd','result','info')
    loginfo.log_close()