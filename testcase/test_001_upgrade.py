__author__ = 'Administrator'
import unittest

from case.upgrade_img import *
from common.log import logger


class UpgardeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.upgrade = Upgrade()
        upgrade = cls.upgrade

    def test_001_upgradeImage(self):
        logger.info("##########测试固件升级##########")
        self.upgrade.upgradeImage()

    @classmethod
    def tearDownClass(cls):
        pass

