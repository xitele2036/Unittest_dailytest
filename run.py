__author__ = 'Administrator'

import unittest
import HTMLTestRunner
import time
import os
# from common.sendmail import SendMail


def run():
    test_dir = './case'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_path = os.path.abspath(".")
    report_name = report_path + '\\report\\testreport\\' + 'TestResult_' + now + '.html'
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
    # mail = SendMail()
    # mail.send()

if __name__=='__main__':
    run()
