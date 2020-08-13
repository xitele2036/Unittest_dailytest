__author__ = 'Administrator'

import time
from case.dut_ssh import *
from common.log import logger

class L2DCN(DUT_SSH):

    def get_dcn_ip(self):
        self.send_cmd1("")
        ip = self.send_cmd1("ifconfig br-dcn |grep 'inet addr'| sed 's/^.*addr://g'| sed 's/Bcast:.*$//g'")
        print(ip)
        return ip

    #设置接口使能状态 0:eth0;1:eth1;2:ath1
    def set_port_status(self,port,status):
        logger.info("**********设置端口状态**********")
        self.send_cmd2("")
        if port =="eth0":
            self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[0].enabled_status="+str(status))
            time.sleep(1)
            value=self.send_cmd2("cfg.lua get ethmanage.@e_port[0].enabled_status")
            # print(type(value))
            if value.strip() == str(status):
                return True
            else:
                return False

        elif port =="eth1":
            self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[1].enabled_status="+str(status))
            value=self.send_cmd2("cfg.lua get ethmanage.@e_port[1].enabled_status")
            if value.strip() == str(status):
                return True
            else:
                return False
        else:
            self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[2].enabled_status="+str(status))
            value=self.send_cmd2("cfg.lua get ethmanage.@e_port[2].enabled_status")
            if value.strip() == str(status):
                return True
            else:
                return False

    def get_port_status(self,port):
        logger.info("**********查询端口状态**********")
        returnVal=None
        self.send_cmd2("")
        if port == "eth0":
            returnVal=self.send_cmd2("cfg.lua get ethmanage.@e_port[0].enabled_status")
        elif port =="eth1":
            returnVal=self.send_cmd2("cfg.lua get ethmanage.@e_port[1].enabled_status")
        else:
            returnVal=self.send_cmd2("cfg.lua get ethmanage.@e_port[2].enabled_status")
        return returnVal

    def set_all_vlanid(self,vlanid):
        logger.info("**********设置所有端口VLAN**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].vlan_id="+str(vlanid))
        self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[0].vlan_id="+str(vlanid))
        self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[1].vlan_id="+str(vlanid))
        return True

    def set_ath1_vlanid(self,vlanid):
        logger.info("**********设置空口VLAN**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].vlan_id="+str(vlanid))
        value=self.send_cmd2("cfg.lua get network.@interface[3].vlan_id")
        if value.strip() ==str(vlanid):
            return True
        else:
            return False

    def get_ath1_vlanid(self):
        logger.info("**********查询空口VLAN**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].vlan_id")
        return returnVal

    def set_eth_vlanid(self,eth,vlanid):
        logger.info("**********设置eth端口VLAN**********")
        self.send_cmd2("")
        if eth == "eth0":
            self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[0].vlan_id="+str(vlanid))
            value = self.send_cmd2("cfg.lua get ethmanage.@e_port[0].vlan_id")
            if value.strip() ==str(vlanid):
                return  True
            else:
                return False
        else:
            self.send_cmd2("cfg.lua set_apply ethmanage.@e_port[1].vlan_id="+str(vlanid))
            value = self.send_cmd2("cfg.lua get ethmanage.@e_port[1].vlan_id")
            if value.strip() ==str(vlanid):
                return  True
            else:
                return False

    def get_eth_vlanid(self,eth):
        logger.info("**********查询eth端口VLAN**********")
        returnVal=None
        self.send_cmd2("")
        if eth == "eth0":
            returnVal=self.send_cmd2("cfg.lua get ethmanage.@e_port[0].vlan_id")
        else:
            returnVal=self.send_cmd2("cfg.lua get ethmanage.@e_port[1].vlan_id")
        return returnVal

    def set_eth_bandwidth(self,bandwidth):
        logger.info("**********设置以太DCN带宽**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].eth_bandwidth="+str(bandwidth))
        value =self.send_cmd2("cfg.lua get network.@interface[3].eth_bandwidth")
        if value.strip() ==str(bandwidth):
            return True
        else:
            return False

    def get_eth_bandwidth(self):
        logger.info("**********查询以太DCN带宽**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].eth_bandwidth")
        return returnVal

    def set_wifi_bandwidth(self,bandwidth):
        logger.info("**********设置空口DCN带宽**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].wifi_bandwidth="+str(bandwidth))
        value=self.send_cmd2("cfg.lua get network.@interface[3].wifi_bandwidth")
        if value.strip() ==str(bandwidth):
            return True
        else:
            return False

    def get_wifi_bandwidth(self):
        logger.info("**********设置空口DCN带宽**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].wifi_bandwidth")
        return returnVal

    def set_static_proto(self,proto):
        logger.info("**********设置DCN IP分配方式**********")
        self.send_cmd2(" ")
        if proto =="static":
            self.send_cmd2("cfg.lua set_apply network.@interface[3].proto='static'")
            self.send_cmd2("cfg.lua set_apply_t network.@interface[3].ipaddr='129.9.2.205' 0")
        else:
            self.send_cmd2("cfg.lua set_apply network.@interface[3].proto='dhcp'")
        time.sleep(1)
        value=self.send_cmd2("cfg.lua get network.@interface[3].proto")
        if value.strip() == proto:
            return True
        else:
            return False

    def get_ip_proto(self):
        logger.info("**********查询DCN IP分配方式**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].proto")
        return returnVal

    def show_dcn_mac(self,proto):
        logger.info("**********查询DCN MAC地址**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua show_dcn_macs "+proto)

    def set_dynamic_macsize(self,size):
        logger.info("**********设置DCN动态MAC地址容量**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].max_mac="+str(size))
        value=self.send_cmd2("cfg.lua get network.@interface[3].max_mac")
        if value.strip() ==str(size):
            return True
        else:
            return False

    def get_dynamic_macsize(self):
        logger.info("**********查询DCN动态MAC地址容量**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].max_mac")
        return returnVal

    def set_static_macsize(self,size):
        logger.info("**********设置DCN静态MAC地址容量**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set network.dcn.static_mac="+str(size))
        value=self.send_cmd2("cfg.lua get network.dcn.static_mac")
        if value.strip() == str(size):
            return True
        else:
            return False

    def get_static_macsize(self):
        logger.info("**********查询DCN静态MAC地址容量**********")
        returnVal=None
        self.send_cmd2("")
        self.send_cmd2("cfg.lua get network.dcn.static_mac")

    def set_mac_agetime(self,agetime):
        logger.info("**********设置DCN动态MAC老化时间**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].age_time="+str(agetime))
        value=self.send_cmd2("cfg.lua get network.@interface[3].age_time")
        if value.strip() == str(agetime):
            return True
        else:
            return False

    def get_mac_agetime(self):
        logger.info("**********查询DCN动态MAC老化时间**********")
        returnVal=None
        self.send_cmd2("")
        returnVal=self.send_cmd2("cfg.lua get network.@interface[3].age_time")
        return returnVal

    def flush_dcn_macs(self):
        logger.info("**********清除DCN 动态MAC**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua flush_dcn_macs")

    def set_priority(self,priority):
        logger.info("**********设置DCN报文优先级**********")
        self.send_cmd2("")
        self.send_cmd2("cfg.lua set_apply network.@interface[3].priority="+str(priority))
        value=self.send_cmd2("cfg.lua get network.@interface[3].priority")
        if value.strip() == str(priority):
            return True
        else:
            return False

if __name__ == "__main__":
    l2dcn = L2DCN()
    l2dcn.get_dcn_ip()
    res1=l2dcn.set_port_status("eth0",0)
    print(res1)
    port_status = l2dcn.get_port_status("eth0")
    print("status:"+port_status)
    # l2dcn.get_eth1_vlanid()
    l2dcn.get_static_macsize()