__author__ = 'Administrator'
import unittest
from case.l2dcn import *
from common.log import logger

class L2DCNTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.l2dcn = L2DCN()
        l2dcn = cls.l2dcn

    def test_001_set_port_status(self):
        logger.info("##########测试端口状态设置##########")
        flag = False
        flag = self.l2dcn.set_port_status("eth0",1)
        self.assertTrue(flag)

    def test_002_set_all_vlanid(self):
        logger.info("##########测试端口vlan设置##########")
        flag = False
        flag = self.l2dcn.set_all_vlanid(4094)
        self.assertTrue(flag)

    def test_003_set_static_proto(self):
        logger.info("##########测试L2DCN IP地址模式设置##########")
        flag = False
        flag = self.l2dcn.set_static_proto("static")
        self.assertTrue(flag)

    def test_004_set_eth_bandwidth(self):
        logger.info("##########测试以太口带宽设置##########")
        flag = False
        flag = self.l2dcn.set_eth_bandwidth(1000)
        self.assertTrue(flag)

    def test_005_set_wifi_bandwidth(self):
        logger.info("##########测试空口带宽设置##########")
        flag = False
        flag = self.l2dcn.set_wifi_bandwidth(1000)
        self.assertTrue(flag)

    def test_006_set_dynamic_macsize(self):
        logger.info("##########测试动态MAC学习容量设置##########")
        flag = False
        flag = self.l2dcn.set_dynamic_macsize(100)
        self.assertTrue(flag)

    def test_007_set_static_macsize(self):
        logger.info("##########测试静态MAC学习容量设置##########")
        flag = False
        flag = self.l2dcn.set_static_macsize(100)
        self.assertTrue(flag)

    def test_008_set_mac_agetime(self):
        logger.info("##########测试动态MAC老化时间设置##########")
        flag = False
        flag = self.l2dcn.set_mac_agetime(100)
        self.assertTrue(flag)

    def test_009_set_priority(self):
        logger.info("##########测试DCN报文优先级设置##########")
        flag = False
        flag = self.l2dcn.set_priority(7)
        self.assertTrue(flag)

    def test_999_get_mac_size(self):
        logger.info("##########测试获取MAC容量##########")
        self.l2dcn.get_dynamic_macsize()

    @classmethod
    def tearDownClass(cls):
        pass

