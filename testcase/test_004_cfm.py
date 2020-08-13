__author__ = 'Administrator'

import unittest
from case.cfm import *
from common.log import logger

class CFMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cfm = CFM()
        abc = cls.cfm

    def test_001_enable_cfm(self):
        logger.info("##########测试使能CFM##########")
        self.cfm.enable_cfm(1)

    def test_002_create_cfm_md(self):
        logger.info("##########测试创建MD##########")
        flag =self.cfm.create_cfm_md("MD0",4)
        self.assertTrue(flag)

    def test_003_create_cfm_ma(self):
        logger.info("##########测试创建MA##########")
        flag =self.cfm.create_cfm_ma("MD0","MA0",1,1000,1)
        self.assertTrue(flag)

    def test_004_create_cfm_mep(self):
        logger.info("##########测试创建MEP##########")
        flag =self.cfm.create_cfm_mep("MD0","MA0",2,2,"ingress")
        self.assertTrue(flag)

    def test_005_create_cfm_mip(self):
        logger.info("##########测试创建MIP##########")
        flag =self.cfm.create_cfm_mip("MD0",2,1)
        self.assertTrue(flag)

    def test_006_apply_cfm_config(self):
        logger.info("##########测试保存CFM配置##########")
        self.cfm.apply_cfm_config()

    def test_007_cfm_cc_status(self):
        logger.info("##########测试CC连通性##########")
        flag=self.cfm.cfm_cc_status()
        self.assertTrue(flag)

    def test_008_LB_test(self):
        logger.info("##########LB 测试##########")
        flag = self.cfm.cfm_LB_test()
        # self.assertTrue(flag)

    def test_009_LT_test(self):
        logger.info("##########LT 测试##########")
        flag=self.cfm.cfm_LT_test()
        self.assertTrue(flag)

    def test_099_show_cfm(self):
        logger.info("##########测试查看CFM配置##########")
        self.cfm.show_cfm_conf()

    @classmethod
    def tearDownClass(cls):
        pass
