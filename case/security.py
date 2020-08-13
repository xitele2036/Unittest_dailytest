__author__ = 'Administrator'

from case.dut_ssh import *
from common.log import logger
from common.ssh_utility import *

class Security(object):

    def __init__(self):
        self.ssh = DUT_SSH()

    #创建只读用户
    def create_readuser(self,username,password):
        logger.info("**********增加只读账户**********")
        self.ssh.send_cmd1("")
        num=self.ssh.send_cmd1("cfg.lua show usermanage | grep =user_cfg | wc -l").strip()
        # print(num)
        self.ssh.send_cmd1("cfg.lua add usermanage user_cfg")
        self.ssh.send_cmd1("cfg.lua set usermanage.@user_cfg[" + num + "].user_level='0' ")
        self.ssh.send_cmd1("cfg.lua set usermanage.@user_cfg[" + num + "].password='Changeme_123' ")
        self.ssh.send_cmd1("cfg.lua set_apply_t usermanage.@user_cfg[" + num + "].user_name='" + str(username) + "' 1")
        result =self.ssh.send_cmd1("cfg.lua show usermanage | grep " + str(username))
        print(result)
        if result.rfind(username) != -1:
            return  True
        else:
            return False

    #创建管理员用户
    def create_superuser(self,username,password):
        logger.info("**********增加管理员账户**********")
        self.ssh.send_cmd1("")
        num=self.ssh.send_cmd1("cfg.lua show usermanage | grep =user_cfg | wc -l").strip()
        # print(num)
        self.ssh.send_cmd1("cfg.lua add usermanage user_cfg")
        self.ssh.send_cmd1("cfg.lua set usermanage.@user_cfg[" + num + "].user_level='1' ")
        self.ssh.send_cmd1("cfg.lua set usermanage.@user_cfg[" + num + "].password='Changeme_123' ")
        self.ssh.send_cmd1("cfg.lua set_apply_t usermanage.@user_cfg[" + num + "].user_name='" + str(username) + "' 1")
        result =self.ssh.send_cmd1("cfg.lua show usermanage | grep " + str(username))
        print(result)
        if result.rfind(username) != -1:
            return  True
        else:
            return False

    #删除指定用户
    def del_user(self,username):
        logger.info("**********删除指定账户**********")
        self.ssh.send_cmd1("")
        self.ssh.send_cmd1("uci show usermanage | grep -w \"@user_cfg\" | grep user_name | grep "+username+" | cut -d'[' -f2 | cut -d']' -f1 | awk '{system(\"cfg.lua del usermanage @user_cfg[\"$0\"] 2\")}'")
        # result=self.ssh.send_cmd("cfg.lua del  usermanage @user_cfg[2] 2")
        result =self.ssh.send_cmd1("cfg.lua show usermanage | grep " + str(username))
        print(result)
        if result.rfind(username) == -1:
            return  True
        else:
            return False

    def login(self,username,password):
        self.ssh.ssh_disconnect()
        flag = False
        try:
            ssh_client = SSHUtility(username,password,"192.168.102.1")
            ssh_client.connect()
            logger.info("**********SSH connect OK**********")
            flag = True
        except Exception as e:
            logger.info("**********SSH connect Error**********")
            flag = False
        finally:
            return flag

if __name__ == "__main__":
    security = Security()
    s1=security.create_readuser("lct2",123)
    print(s1)
    security.create_superuser("lct3",123)
    security.del_user("lct2")
    ss=security.login("lct2","Changeme_123")
    print(ss)