#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:文本：读取文件里的数据,生成web_info 和 user_list
"""

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

if __name__ == '__main__':
    # info = get_webinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\webinfo.txt')
    # for key in info:
    #     print(key,info[key])
    info = get_userinfo(r'D:\python_pycharmWorkspace\python36\Web_Test_Selenium\study\DataSeparation\userinfo.txt')
    print(info)
