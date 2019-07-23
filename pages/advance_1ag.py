
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from common.logger import Logger

class Advance1AG(BasePage):

    # advance_loc = (By.XPATH, "//img[@id='down_pic']")
    # advanc_dcnpage_loc = (By.XPATH, "//*[@id=\"Dcnpage_Select\"]/span/a")
    # editbtn_loc = (By.XPATH, "//*[@id='button_dcn_edit']")
    #
    # dcn_eth0_status_loc = (By.ID, "icon_eth0_dcn_enable")
    # dcn_eth0_disable_loc = (By.XPATH, "//ul[@id='ul_eth0_dcn_enable']/li[1]")
    # dcn_eth0_enable_loc = (By.XPATH, "//ul[@id='ul_eth0_dcn_enable']/li[2]")
    # dcn_eth0_vlan_loc = (By.XPATH, "//*[@id='input_eth0_dcn_vlan_id']")
    #
    # dcn_eth1_status_loc = (By.ID, "icon_eth1_dcn_enable")
    # dcn_eth1_disable_loc = (By.XPATH, "//ul[@id='ul_eth1_dcn_enable']/li[1]")
    # dcn_eth1_enable_loc = (By.XPATH, "//ul[@id='ul_eth1_dcn_enable']/li[2]")
    # dcn_eth1_vlan_loc = (By.XPATH, "//*[@id='input_eth1_dcn_vlan_id']")
    #
    # dcn_ath1_status_loc = (By.ID, "icon_ath1_dcn_enable")
    # dcn_ath1_disable_loc = (By.XPATH, "//ul[@id='ul_ath1_dcn_enable']/li[1]")
    # dcn_ath1_enable_loc = (By.XPATH, "//ul[@id='ul_ath1_dcn_enable']/li[2]")
    #
    # dcn_save_btn_loc = (By.XPATH, "//*[@id='div_dcn_detail']/div[2]/button[1]")

    # def __init__(self):
    #     self.log = Logger()
    #     self.logger = self.log.creatLogger()

    def enterAdvance1AG(self):
        # noinspection PyBroadException
        log = Logger()
        log.info("点击高级功能，进入OAM配置页面")
        try:
            self.find_element_by_xpath("//img[@id='down_pic']").click()
        except:
            pass
        sleep(1)
        self.find_element_by_xpath("//*[@id=\"Oampage_Select\"]/span/a").click()

    def setOAMStatus(self, status):
        sleep(30)
        # oam_status = self.find_element_by_xpath("//*[@id=\"input_oam_enable\"]").text
        # print(oam_status)
        # if(oam_status == )
        self.find_element_by_xpath("//*[@id=\"icon_oam_enable\"]").click()
        # self.find_element_by_xpath("//*[@id=\"ul_oam_enable\"]/li[1]").click()
        self.find_element_by_xpath("//*[@id=\"ul_oam_enable\"]/li[1]").click()
        self.find_element_by_xpath("//*[@id=\"btn_save_oam_enable\"]").click()
        sleep(30)

    def addMD(self,md_name,level=4):
        self.find_element_by_xpath("//*[@id=\"btn_div_add_md\"]").click()
        self.find_element_by_xpath("//*[@id=\"input_md_name\"]").send_keys(md_name)
        self.find_element_by_xpath("//*[@id=\"icon_md_level\"]").click()
        self.find_element_by_xpath("//ul[@id='ul_md_level']//li[@class='el-select-dropdown__item'][contains(text(),'" + str(level) + "')] ").click()
        self.find_element_by_xpath("//*[@id='div_add_md']/div/div[3]/button[1]").click()

    def delMD(self,name):
        pass

    def addMA(self,md_name,ma_name,service,period,rm_mep):
        self.find_element_by_xpath("//*[@id='btn_div_add_ma']").click()
        #配置MD
        self.find_element_by_xpath("//*[@id='icon_ma_md_name']").click()
        self.find_element_by_xpath("//*[@id='icon_ma_md_name']//li[@class='el-select-dropdown__item'][contains(text(),'" + md_name + "')] ").click()
        #配置MA
        self.find_element_by_xpath("//*[@id='input_ma_name']").send_keys(ma_name)
        #选择业务
        self.find_element_by_xpath("//*[@id='icon_ma_relevant_service']").click()
        self.find_element_by_xpath("")
        #配置CC 周期
        self.find_element_by_xpath("//*[@id='input_ma_period']").click()
        self.find_element_by_xpath("//*[@id='ul_ma_period']/li[@class='el-select-dropdown__item'][@value="+period+"]").click()
        #配置remote mep id
        self.find_element_by_xpath("//*[@id='input_remote_mep_id']").send_keys(rm_mep)
        #保存设置
        self.find_element_by_xpath("//*[@id='div_add_ma']/div/div[3]/button[1]").click()

    def delMA(self):
        pass

    def addMIP(self,md_name,port,mip_index):
        self.find_element_by_xpath("//*[@id='btn_div_add_mip']").click()
        self.find_element_by_xpath("//*[@id='icon_mip_md_name']").click()
        self.find_element_by_xpath("//*[@id='MD0']").click()
        # mip_li = self.find_elements_by_xpath("//*[@id='ul_mip_md_name']")
        # print(mip_li)
        # for mip in mip_li:
        #     # print(mip)
        #     # if mip.find_element_by_xpath("./[@class='el-select-dropdown__item'][contains(@value),'MD0']").text() == md_name:
        #     print(mip.find_element_by_xpath("//*[@id='MD0']").click())
                # mip.find_element_by_xpath("./li[contains(text(),"+md_name+")").click()
        self.find_element_by_xpath("//*[@id='ul_mip_port']/li[@class='el-select-dropdown__item'][contains(text(),'" + port + "')]").click()
        self.find_element_by_id("input_mip_mip_id").send_keys(mip_index)
        #保存MIP配置
        self.find_element_by_xpath("//*[@id='div_add_mip']/div/div[3]/button[1]/span").click()

    def delMIP(self):
        pass

    def addMEP(self,md_name,ma_name,port,vlan,mep_id,direction,cc_status):
        self.find_element_by_xpath("//*[@id='btn_div_add_mep']").click()
        self.find_element_by_xpath()

    def delMEP(self):
        pass




    def saveOAMConf(self):
        self.find_element("//*[@id=\"btn_oam_all_settings\"]").click()
        sleep(30)

    def LBTest(self):
        pass

    def LTTest(self):
        pass
