__author__ = 'Administrator'

import time
from case.dut_ssh import *
from common.log import logger

class CFM(DUT_SSH):

    #使能/不使能cfm
    def enable_cfm(self,status):
        logger.info("**********使能CFM**********")
        self.send_cmd1("")
        self.send_cmd1("cfg.lua set cfm.@cfm[0].enable=" + str(status))
        value = self.send_cmd2("cfg.lua get cfm.@cfm[0].enable")
        if int(value.strip()) == 1:
            return True
        else:
            return False

    #创建MD
    # def create_cfm_md(self):
    def create_cfm_md(self,md_name,md_level):
        logger.info("**********创建 CFM MD**********")
        self.send_cmd1("")
        cnt = self.send_cmd1("uci show cfm | grep -w \"@md\"|grep "+md_name+" | wc -l")
        # print("cnt:"+cnt)
        self.send_cmd1("cfg.lua add cfm md 1")
        self.send_cmd1("cfg.lua set cfm.@md[0].md_name="+md_name)
        self.send_cmd1("cfg.lua set cfm.@md[0].md_level="+str(md_level))
        self.send_cmd1("cfg.lua set cfm.@md[0].md_index="+str(int(cnt)+1))
        self.send_cmd1("cfg.lua add cfm md 2")
        value = self.send_cmd1("uci show cfm | grep -w \"@md\"|grep "+ md_name +" | wc -l")
        # print("cnt:"+value)
        if int(value.strip()) == 1:
            return True
        else:
            return False

    #删除MD
    def del_cfm_md(self):
        logger.info("**********删除 CFM MD**********")
        self.send_cmd1("cfg.lua del cfm @md[0]")

    #创建MA
    # def create_cfm_ma(self):
    def create_cfm_ma(self,md_name,ma_name,service_id,cc_period,rmep_id):
        logger.info("**********创建 CFM MA**********")
        self.send_cmd1("")
        cnt = self.send_cmd1("uci show cfm | grep -w \"@ma\"|grep ma_name | wc -l")
        # print("cnt:"+cnt)
        self.send_cmd1("cfg.lua add cfm ma 1")
        self.send_cmd1("cfg.lua set cfm.@ma[0].md_name=" + md_name)
        self.send_cmd1("cfg.lua set cfm.@ma[0].ma_name=" + ma_name)
        self.send_cmd1("cfg.lua set cfm.@ma[0].ma_index="+str(int(cnt)+1))
        self.send_cmd1("cfg.lua set cfm.@ma[0].service_id=" + str(service_id))
        self.send_cmd1("cfg.lua set cfm.@ma[0].cc_period="+str(cc_period))
        self.send_cmd1("cfg.lua set cfm.@ma[0].remote_mep_id=" + str(rmep_id))
        self.send_cmd1("cfg.lua add cfm ma 2")
        value = self.send_cmd1("uci show cfm | grep -w \"@ma\"|grep "+ ma_name +" | wc -l")
        # print("cnt:"+value)
        if int(value.strip()) == 1:
            return True
        else:
            return False

    #删除MA
    def del_cfm_ma(self):
        logger.info("**********删除 CFM MA**********")
        self.send_cmd1("cfg.lua del cfm @ma[0]")

    #创建MEP
    # def create_cfm_mep(self):
    def create_cfm_mep(self,md_name,ma_name,port_id,mep_id,direction):
        logger.info("**********创建 CFM MEP**********")
        self.send_cmd1("")
        self.send_cmd1("cfg.lua add cfm mep 1")
        self.send_cmd1("cfg.lua set cfm.@mep[0].md_name="+md_name)
        self.send_cmd1("cfg.lua set cfm.@mep[0].ma_name="+ma_name)
        self.send_cmd1("cfg.lua set cfm.@mep[0].port_id="+str(port_id))
        self.send_cmd1("cfg.lua set cfm.@mep[0].mep_id="+str(mep_id))
        self.send_cmd1("cfg.lua set cfm.@mep[0].cc_status='1'")
        self.send_cmd1("cfg.lua set cfm.@mep[0].vlan='2'")
        self.send_cmd1("cfg.lua set cfm.@mep[0].direction="+direction)
        self.send_cmd1("cfg.lua add cfm mep 2")
        value = self.send_cmd1("uci show cfm | grep -w \"@mep\"|grep "+ ma_name +" | wc -l")
        # print("cnt:"+value)
        if int(value.strip()) == 1:
            return True
        else:
            return False

    #删除MEP
    def del_cfm_mep(self):
        logger.info("**********删除 CFM MEP**********")
        self.send_cmd1("cfg.lua del cfm @mep[0]")

    #创建MIP
    def create_cfm_mip(self,md_name,port_id,mip_id):
    # def create_cfm_mip(self):
        logger.info("**********创建 CFM MIP**********")
        self.send_cmd1("")
        self.send_cmd1("cfg.lua add cfm mip 1")
        self.send_cmd1("cfg.lua set cfm.@mip[0].md_name=" +md_name)
        self.send_cmd1("cfg.lua set cfm.@mip[0].port_id="+str(port_id))
        self.send_cmd1("cfg.lua set cfm.@mip[0].mip_id="+str(mip_id))
        self.send_cmd1("cfg.lua add cfm mip 2")
        value = self.send_cmd1("uci show cfm | grep -w \"@mip\"|grep "+ md_name +" | wc -l")
        # print("cnt:"+value)
        if int(value.strip()) == 1:
            return True
        else:
            return False

    #删除MIP
    def del_cfm_mip(self):
        logger.info("**********删除 CFM MIP**********")
        self.send_cmd1("cfg.lua del cfm @mip[0]")

    #设置CC周期
    def set_cc_period(self,cc_period):
        logger.info("**********设置CC周期**********")
        self.send_cmd1("")
        self.send_cmd1("cfg.lua set cfm.@ma[0].cc_period=" + str(cc_period))

    #保存cfm配置
    def apply_cfm_config(self):
        self.send_cmd1("")
        self.send_cmd1("cfg.lua set_apply cfm.@cfm[0].action='1'")
        time.sleep(5)

    #查看CC状态
    def cfm_cc_status(self):
        logger.info("**********查看CC状态**********")
        self.send_cmd1("")
        # res = self.send_cmd1("cfm_utility -m query | grep \"Link Up\" | wc -l")
        res = self.send_cmd1("cfm_utility -m query")
        # print(res)
        logger.info(res)
        if res.find("Link Up")!=-1:
            return True
        return False


    #LB测试
    def cfm_LB_test(self):
        logger.info("**********开始LB测试**********")
        self.send_cmd1("")
        res=self.send_cmd1("cfm_utility -m lb -i 2 1")
        # print(res)
        logger.info(res)

    #LT测试
    def cfm_LT_test(self):
        logger.info("**********开始LT测试**********")
        self.send_cmd1("")
        res = self.send_cmd1("cfm_utility -m lt -i 2 1\n")
        # print(res)
        logger.info(res)
        if res.find("RlyHit")!= -1:
            return True
        return False

    def show_cfm_conf(self):
        logger.info("**********查看CFM配置**********")
        self.send_cmd1("")
        self.send_cmd1("uci show cfm")

    #查看cfm告警
    def check_cfm_alm(self,alm):
        logger.info("**********查看当前告警**********")
        self.send_cmd1("")
        alm_cmd ="alm_get_cur | grep "+ alm +" |wc -l"
        count = self.send_cmd1(alm_cmd)
        print(count)

if __name__ == "__main__":
    cfm = CFM()
    cfm.enable_cfm(1)
    cfm.create_cfm_md("MD0",4)
    cfm.create_cfm_ma("MD0","MA0",1,1000,1)
    cfm.create_cfm_mep("MD0","MA0",2,2,"ingress")
    cfm.create_cfm_mip("MD0",2,1)
    cfm.apply_cfm_config()
    cfm.show_cfm_conf()
    dd=cfm.cfm_cc_status()
    print(dd)
    cfm.cfm_LB_test()
    tt=cfm.cfm_LT_test()
    print(tt)
    cfm.check_cfm_alm("ETH_LOS")
