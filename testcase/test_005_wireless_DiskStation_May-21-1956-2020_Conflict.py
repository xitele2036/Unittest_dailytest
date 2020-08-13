__author__ = 'Administrator'

import unittest
from case.wireless import *
from common.log import logger

class WirelessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wl = Wireless()
        wl = cls.wl

    def test_001_connect_stat(self):
        logger.info("##########测试无线连接状态##########")
        flag = False
        flag = self.wl.get_connect_stat()
        self.assertTrue(flag)

    @classmethod
    def tearDownClass(cls):
        pass
