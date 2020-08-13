__author__ = 'Administrator'

from case.dut_ssh import DUT_SSH
import subprocess
import re
from common.log import logger
from common.ftp import *

class CheckUpgrade(object):

    def ping_dut(self,ip):
        logger.info("**********开始Ping设备**********")
        file_out = subprocess.Popen('ping %s\n' %ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            line = file_out.stdout.read().strip().decode("gbk")
            # print("line:"+line)
            res = re.search(r'TTL', line, re.M | re.I)
            if res:
                return True   # 成功
            else:
                return False  # 失败

    def check_ver(self):
        logger.info("**********检查设备当前版本**********")
        #获取最新固件子版本号
        version = img_name.split(".")[2]
        # print("version:" +version)
        ssh = DUT_SSH()
        res= ssh.send_cmd1("cfg.lua get_version")
        fw_info = res.splitlines()
        # print(fw_info)
        fw_ver=fw_info[0].split(":")[1].split(".")[3]
        if fw_ver == version:
            return True
        else:
            return  False

if __name__ == "__main__":
    chkupgrade = CheckUpgrade()
    res1=chkupgrade.ping_dut("192.168.102.1")
    print(res1)
    if res1 == 0:
        time.sleep(120)
    res2=chkupgrade.check_ver()
    print(res2)


