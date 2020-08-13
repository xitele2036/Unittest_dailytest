__author__ = 'Administrator'

from time import sleep
from case.dut_ssh import *
from common.log import logger

class Wireless(DUT_SSH):

    def get_connect_stat(self):
        logger.info("**********查看无线连接情况**********")
        self.send_cmd1("")
        result=self.send_cmd1("cfg.lua get_connected_ap | grep 9c:b7:93 | wc -l")
        if int(result)!=0:
            return True
        return False

    def get_mode(self):
        pass

    def set_country(self,country):
        pass

    def get_cur_country(self):
        logger.info("**********查看当前生效的国家**********")
        result=self.send_cmd2("cfg.lua get_cur wireless.@wifi-device[1].country")

if __name__ == "__main__":
    wl =Wireless()
    vlaue=wl.get_connect_stat()
    print(vlaue)