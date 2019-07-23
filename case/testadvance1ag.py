
from time import sleep
import unittest

from pages.browser import Browser
from pages.login import Login
from pages.advance_1ag import Advance1AG
from common.logger import Logger
from config import globalparameter


class Advance1AGTest(unittest.TestCase):
    def setUp(self):
        self.log = Logger()

        browser = Browser()
        self.driver = browser.openBrowser()
        self.login = Login(self.driver)
        self.login.open("https://"+globalparameter.dut_ip)
        sleep(10)
        self.login.sendUserName(globalparameter.dut_user)
        self.login.sendPasswd(globalparameter.dut_passwd)
        self.login.clickLoginBtn()

    def testAdvance1AG(self):
        self.log.info("**************Start Test 1AG *************")
        oam = Advance1AG(self.driver)
        oam.enterAdvance1AG()
        # oam.setOAMStatus("enable")
        # oam.addMD("MD14",7)
        oam.addMIP("MD0","2-EG2-1",1)

        self.log.info("************* OAM 1AG End**************")

    def tearDown(self):
        self.login.logout()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
