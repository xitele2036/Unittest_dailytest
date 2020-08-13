__author__ = 'Administrator'

import unittest
from case.security import *
from common.log import logger

class SecurityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.security = Security()
        security = cls.security

    def test_001_create_readuser(self):
        logger.info("##########测试新增只读用户##########")
        flag = False
        flag=self.security.create_readuser("lct2","Changeme_123")
        self.assertTrue(flag)

    def test_002_create_superuser(self):
        logger.info("##########测试新增管理员用户##########")
        flag = False
        flag=self.security.create_superuser("lct3","Changeme_123")
        self.assertTrue(flag)

    def test_003_del_user(self):
        logger.info("##########测试删除用户##########")
        flag = False
        flag=self.security.del_user("lct3")
        self.assertTrue(flag)

    def test_004_login(self):
        logger.info("##########测试用户登录##########")
        flag = False
        flag=self.security.login("lct2","Changeme_123")
        self.assertTrue(flag)

    @classmethod
    def tearDownClass(cls):
        pass

