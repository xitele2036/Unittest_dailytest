import configparser
import os
from pathlib import Path

class ReadConfig(object):
    def __init__(self):

        self.conf_dir = os.path.realpath('..\config\config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(self.conf_dir)

    def getConfVal(self,section,option):
        return self.cf.get(section,option)
