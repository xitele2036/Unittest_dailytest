import configparser
import os,sys
from common.readconfig import  ReadConfig

# config = ReadConfig()
# config_file_path = os.path.split(os.path.realpath(__file__))[0]
# print(os.path.join(config_file_path,'config.ini'))
# config = ReadConfig(os.path.join(config_file_path,'config.ini'))

# config_file_path = os.path.realpath("/dailytest/config/config.ini")
config_file_path = os.path.realpath("."+"/config.ini")
print(os.path.realpath("."+"/config.ini"))
print(config_file_path)
config = ReadConfig(config_file_path)

#COMMON Section
run_mode =config.getConfVal("COMMON","run_mode")
browser = config.getConfVal("COMMON","browser")

#DUT Section
dut_ip = config.getConfVal("DUT","dut_ip")
dut_user = config.getConfVal("DUT","dut_user")
dut_passwd = config.getConfVal("DUT","dut_passwd")

#SSH Section
ssh_user1 = config.getConfVal("SSH","ssh_user1")
ssh_passwd1 = config.getConfVal("SSH","ssh_passwd1")

#EMAIL Section
