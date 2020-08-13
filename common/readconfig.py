import configparser


class ReadConfig(object):
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfVal(self,section,option):
        return self.cf.get(section,option)
