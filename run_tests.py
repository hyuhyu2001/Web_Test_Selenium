#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:jinzj
@contact:
@others:
@desc:
"""
import time, sys, os
sys.path.append('./test_case')
sys.path.append('./public_web')
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(filename):
    mail_host='SMTP.cloud-young.com'#smtp.exmail.qq.com
    mail_user='jinzj@cloud-young.com'
    mail_pass='Jinzj1'

    sender='jinzj@cloud-young.com'
    receivers=['jinzj@cloud-young.com']

    message = MIMEMultipart('related')

    f = open(filename, 'rb')
    mail_body = f.read()
    # 添加正文
    msg = MIMEText(mail_body, 'html', 'utf-8')
    message.attach(msg)
    # 添加附件，附件需要添加到正文后，否则mac版自带邮箱收不到内容
    att = MIMEText(mail_body, 'base64', 'uft-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att)
    f.close()

    message['From'] = sender
    message['To'] = ",".join(receivers)
    message['Subject'] = Header("测试报告", 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())


def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    filename = os.path.join(testreport, lists[-1])
    print(filename)
    return filename


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Web Selenium Test Report',
                            description='The results are following:')
    runner.run(discover)
    fp.close()

    test_report = './report'
    rep = report(test_report)
    send_email(rep)