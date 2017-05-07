#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:增加日志输出，文本
测试结果（包含错误元素信息）保存到数据文件
log_write(self,msg)：写日志
log_close(self)：关闭日志文件
"""

import time

class Logiofo(object):
    def __init__(self,path='',mode='w'):
        fname =  path + time.strftime('%Y-%m-%d',time.gmtime())
        self.log = open(path + fname + '.txt',mode)

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()

if __name__ == '__main__':
    log = Logiofo()
    log.log_write('test Loginfo 测试')
    log.log_close()