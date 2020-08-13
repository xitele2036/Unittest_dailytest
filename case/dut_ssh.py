__author__ = 'Administrator'

from common.ssh_utility import *
from config.globalparameter import *
from common.log import logger

class DUT_SSH(object):

    def __init__(self,username=ssh_user1,password=ssh_passwd1,host=dut_ip):
        try:
            self.ssh_client = SSHUtility(username,password,host)
            self.ssh_client.connect()
            logger.info("**********SSH connect OK**********")
        except Exception as e:
            logger.info("**********SSH connect Error**********")

    # 发送命令并返回原始结果
    def send_cmd1(self,cmd):
        if cmd.strip() !='':
            logger.info(cmd)
        result = self.ssh_client.send1(cmd)
        return result

    # 发送命令返回经过解析后的结果，不带result:
    def send_cmd2(self,cmd):
        if cmd.strip() !='':
            logger.info(cmd)
        result=self.ssh_client.send2(cmd)
        return result

    # 发送命令等待一段时间才会有返回原始结果
    def send_cmd3(self,cmd,timeout):
        if cmd.strip() !='':
            logger.info(cmd)
        result = self.ssh_client.send3(cmd,timeout)
        return result

    #断开SSH 连接
    def ssh_disconnect(self):
        try:
            self.ssh_client.close()
            logger.info("**********SSH disconnect OK**********")
        except Exception as e:
            logger.info("**********SSH disconnect Error**********")

    # def __del__(self):
    #     self.ssh_disconnect()


if __name__ == "__main__":
    ssh = DUT_SSH("lct","Changeme_123","192.168.102.1")
    ssh.send_cmd1("\n")
    res=ssh.send_cmd1("cfg.lua get_version")
    print(res)