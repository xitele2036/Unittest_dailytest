__author__ = 'Administrator'
import unittest
from case.check_ver import *
from common.log import logger

class CheckTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chkupgrade = CheckUpgrade()
        chkupgrade = cls.chkupgrade

    def test_001_checkping(self):
        time.sleep(60*10)
        flag = False
        for i in  range(3):
            res = self.chkupgrade.ping_dut("192.168.102.1")
            if(res == 1):
                flag = True
                break
            time.sleep(60)
        self.assertTrue(flag)
    def test_002_check_ver(self):
        logger.info("##########测试升级结果##########")
        res = self.chkupgrade.check_ver()
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        pass

