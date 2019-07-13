import configparser
import os
from pathlib import Path

class ReadConfig(object):
    def __init__(self,filename):

        # self.conf_dir = os.path.realpath('..\config\config.ini')
        # self.conf_dir = os.path.realpath('..\config\config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfVal(self,section,option):
        return self.cf.get(section,option)
