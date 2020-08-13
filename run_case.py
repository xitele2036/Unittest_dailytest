__author__ = 'Administrator'

import unittest
import HTMLTestRunner
import time
import os
from common.sendmail import SendMail
from config import globalparameter

def run():

    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_path = os.path.abspath(".")
    report_name = report_path + '\\report\\html\\' + 'TestResult_' + now + '.html'
    # print(report_name)
    with open(report_name,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='RTN510 web 自动化测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = SendMail()
    mail.send()

# while True:
#     time_now = time.strftime("%H:%M:%S", time.localtime())
#     # print(time_now)
#     if time_now == "14:05:00":
#         run()