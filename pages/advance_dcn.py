
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from common.logger import Logger

class AdvanceDCN(BasePage):

    advance_loc = (By.XPATH, "//img[@id='down_pic']")
    advanc_dcnpage_loc = (By.XPATH, "//*[@id=\"Dcnpage_Select\"]/span/a")
    editbtn_loc = (By.XPATH, "//*[@id='button_dcn_edit']")

    dcn_eth0_status_loc = (By.ID, "icon_eth0_dcn_enable")
    dcn_eth0_disable_loc = (By.XPATH, "//ul[@id='ul_eth0_dcn_enable']/li[1]")
    dcn_eth0_enable_loc = (By.XPATH, "//ul[@id='ul_eth0_dcn_enable']/li[2]")
    dcn_eth0_vlan_loc = (By.XPATH, "//*[@id='input_eth0_dcn_vlan_id']")

    dcn_eth1_status_loc = (By.ID, "icon_eth1_dcn_enable")
    dcn_eth1_disable_loc = (By.XPATH, "//ul[@id='ul_eth1_dcn_enable']/li[1]")
    dcn_eth1_enable_loc = (By.XPATH, "//ul[@id='ul_eth1_dcn_enable']/li[2]")
    dcn_eth1_vlan_loc = (By.XPATH, "//*[@id='input_eth1_dcn_vlan_id']")

    dcn_ath1_status_loc = (By.ID, "icon_ath1_dcn_enable")
    dcn_ath1_disable_loc = (By.XPATH, "//ul[@id='ul_ath1_dcn_enable']/li[1]")
    dcn_ath1_enable_loc = (By.XPATH, "//ul[@id='ul_ath1_dcn_enable']/li[2]")

    dcn_save_btn_loc = (By.XPATH, "//*[@id='div_dcn_detail']/div[2]/button[1]")

    # def __init__(self):
    #     self.log = Logger()
    #     self.logger = self.log.creatLogger()

    def goAdvanceNetwork(self):
        # noinspection PyBroadException
        log = Logger()
        log.info("点击高级功能，进入DCN配置页面")
        try:
            self.find_element_by_xpath("//img[@id='down_pic']").click()
        except:
            pass
        sleep(1)
        self.find_element_by_xpath("//*[@id=\"Dcnpage_Select\"]/span/a").click()

    def editDCNConf(self):
        # log.info("点击DCN Edit 按钮")
        self.find_element_by_xpath("//*[@id='button_dcn_edit']").click()
        sleep(5)

    def setDCNPort(self, port, status):
        if ('eth0' == port):
            dcn_icon = self.find_element_by_id("icon_eth0_dcn_enable").click()

            # eth0 dcn关闭
            #eth0_port = driver.find_element_by_xpath("//ul[@id='ul_eth0_dcn_enable']/li[1]").click()

            #eth0 dcn启用
            eth0_port = self.find_element(*self.dcn_eth0_enable_loc).click()

        elif ('eth1' == port):
            dcn_icon = self.find_element(*self.dcn_eth1_status_loc).click()

            # eth1 dcn关闭
            #eth1_port = driver.find_element_by_xpath("//ul[@id='ul_eth0_dcn_enable']/li[1]").click()

            #eth1 dcn启用
            #eth1_port = driver.find_element_by_xpath("//ul[@id='ul_eth1_dcn_enable']/li[1]").click()
            eth1_port = self.find_element(*self.dcn_eth1_enable_loc).click()

        else:
            dcn_icon = self.find_element(*self.dcn_ath1_status_loc).click()

            # ath1 dcn关闭
            #ath1_port = driver.find_element_by_xpath("//ul[@id='ul_eth0_dcn_enable']/li[1]").click()

            #ath1 dcn启用
            ath1_port = self.find_element(*self.dcn_ath1_enable_loc).click()


    def setPortVlan(self, port, vlanid):
        if (port == 'eth0'):
            # modify eth0 vlan id
            self.find_element(*self.dcn_eth0_vlan_loc).clear()
            self.find_element(*self.dcn_eth0_vlan_loc).send_keys(vlanid)
        elif (port == 'eth1'):
            # modify eth1 vlan id
            self.find_element(*self.dcn_eth1_vlan_loc).clear()
            self.find_element(*self.dcn_eth1_vlan_loc).send_keys(vlanid)
        else:
            pass

    def getDCNConf(self, port):

        eth0_dcn_name = self.find_element_by_xpath("//*[@id='dcn_port_name_0']").text
        eth0_dcn_status = self.find_element_by_xpath("//*[@id='div_dcn_access_list']/li[1]/div[2]").text
        eth0_dcn_proto = self.find_element_by_xpath("//*[@id='dcn_porttype_0']").text
        eth0_dcn_vlan = self.find_element_by_xpath("//*[@id='dcn_vlanid_0']").text


        eth1_dcn_name = self.find_element_by_xpath("//*[@id='dcn_port_name_1']").text
        eth1_dcn_status = self.find_element_by_xpath("//*[@id='div_dcn_access_list']/li[2]/div[2]").text
        eth1_dcn_proto = self.find_element_by_xpath("//*[@id='dcn_porttype_1']").text
        eth1_dcn_vlan = self.find_element_by_xpath("//*[@id='dcn_vlanid_1']").text

        ath1_dcn_name = self.find_element_by_xpath("//*[@id='dcn_port_name_2']").text
        ath1_dcn_status = self.find_element_by_xpath("//*[@id='div_dcn_access_list']/li[3]/div[2]").text
        ath1_dcn_proto = self.find_element_by_xpath("//*[@id='dcn_porttype_2']").text
        ath1_dcn_vlan = self.find_element_by_xpath("//*[@id='dcn_vlanid_2']").text


    def saveDCNConf(self):
        self.find_element(*self.dcn_save_btn_loc).click()

    #save_btn = driver.find_element_by_xpath("//*[@id='div_dcn_detail']/div[2]/button[1]").click()

