__author__ = 'Administrator'

from time import sleep
from common.ftp import *
from case.dut_ssh import *
from common.log import logger

class Upgrade(DUT_SSH):

    # def get_imge(self):
    #     ftp =FTPClient()
    #     img_path,img_name = ftp.get_imge()
    #     return img_path,img_name

    def upgradeImage(self):
        logger.info("**********下载最新固件**********")
        download_cmd = "cd /tmp && tftp -g -l {} {}".format(img_name,"192.168.102.2")
        print("down:"+ download_cmd)
        self.send_cmd1(download_cmd)
        self.send_cmd1("ls -al")
        sleep(120)
        logger.info("**********升级最新固件**********")
        upgrade_cmd = "sysupgrade /tmp/{}".format(img_name)
        print("upgrade:"+upgrade_cmd)
        self.send_cmd1(upgrade_cmd)
        sleep(20)

if __name__ == "__main__":
    upgrade = Upgrade()
    upgrade.upgradeImage()


