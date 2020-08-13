
from ftplib import FTP
import tarfile
import os,time,shutil
import datetime

class FTPClient():

    def __init__(self):
        self.filename = "image_20190906_huawei_Debug_01.tar.gz"
        self.img_name = "R3_V1.0.1580.dakota_huawei_Debug_20190902.img"
        try:
            self.ftp = FTP()
            port = 21

            self.ftp.connect('218.94.146.74', port)
            self.ftp.encoding = 'GB18030'
            self.ftp.login('public', 'public')
        except IOError as err:
            raise IOError("ftp connect failed!")

    def __del__(self):
        self.ftp.quit()

    def dl_file(self):
        day = datetime.datetime.now().strftime("%Y%m%d")
        filename = "image_"+day+"_huawei_Debug_01.tar.gz"
        print("filename="+filename)
        self.ftp.cwd('研发相关/Huawei_R3固件/')
        # print(self.ftp.dir())

        flag = False
        filelist = [] #to store all files
        self.ftp.retrlines('NLST',filelist.append)    # append to list
        filelist.reverse()
        for f in filelist:
            print("file="+ f)
            time.sleep(0.5)
            if f == filename:
                flag =True
                break

        time.sleep(2)
        # dir_path = os.path.abspath("D:/dailytest/fw/")
        dir_path = "D:/dailytest/fw/"
        # print(dir_path)
        path = dir_path+'{0}'.format(filename)
        f = open(path, 'wb')
        time.sleep(1)
        self.ftp.retrbinary('RETR ' + filename, f.write)
        f.close()
        time.sleep(1)
        # print(dir_path)

    def unzip_file(self):
        day = datetime.datetime.now().strftime("%Y%m%d")
        filename = "image_"+day+"_huawei_Debug_01.tar.gz"
        print("filename="+filename)

        dir_path = "D:/dailytest/fw/"
        print(dir_path)
        path = dir_path+'{0}'.format(filename)
        f = open(path, 'wb')
        time.sleep(1)
        self.ftp.retrbinary('RETR ' + filename, f.write)
        f.close()
        time.sleep(1)
        # print(dir_path)
        #如果存在原目录，则先删除在解压
        des_file = dir_path+"/products"
        if(os.path.exists(des_file)):
            # print("存在原始路径")
            shutil.rmtree(des_file)
        print("path:"+path)
        tar = tarfile.open(path)
        tar.extractall(path = os.path.realpath(dir_path))
        tar.close()
        self.img_path,self.img_name=self.find_file_name(des_file)
        shutil.copy(self.img_path,dir_path)
        # print("fw file:"+ll)
        # print("ff:"+ff)
        return self.img_path,self.img_name

    def get_imge(self):
        # day = datetime.datetime.now().strftime("%Y%m%d")
        # filename = "image_"+day+"_huawei_Debug_01.tar.gz"
        # print("filename="+filename)
        # self.ftp.cwd('研发相关/Huawei_R3固件/')
        # # print(self.ftp.dir())
        #
        # flag = False
        # filelist = [] #to store all files
        # self.ftp.retrlines('NLST',filelist.append)    # append to list
        # filelist.reverse()
        # for f in filelist:
        #     print("file="+ f)
        #     time.sleep(0.5)
        #     if f == filename:
        #         flag =True
        #         break
        #
        # time.sleep(2)
        # # dir_path = os.path.abspath("D:/dailytest/fw/")
        # dir_path = "D:\\dailytest\\fw\\"
        # print(dir_path)
        # path = dir_path+'{0}'.format(filename)
        # f = open(path, 'wb')
        # time.sleep(1)
        # self.ftp.retrbinary('RETR ' + filename, f.write)
        # f.close()
        # time.sleep(1)
        # print(dir_path)
        # #如果存在原目录，则先删除在解压
        # des_file = dir_path+"\\products"
        # if(os.path.exists(des_file)):
        #     print("存在原始路径")
        #     shutil.rmtree(des_file)
        # print("path:"+path)
        # tar = tarfile.open(path)
        # # tar.extractall(path = os.path.realpath("/dailytest/fw/"))
        # tar.extractall(path = os.path.realpath(dir_path))
        # tar.close()
        # ll,ff=self.get_file_name(des_file)
        #
        # # mv_cmd="copy " +ll +" "+dir_path
        # # os.system(mv_cmd)
        # shutil.copy(ll,dir_path)
        # print("fw file:"+ll)
        # print("ff:"+ff)
        # return ll,ff

        # ftpclient = FTPClient()
        # ftpclient.get_imge()
        self.dl_file()
        s1,s2 = self.unzip_file()
        # print(s1)
        # print(s2)
        return s1,s2

    def find_file_name(self,file_dir):
        L=[]
        ff=''
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.img':
                    L.append(os.path.join(root, file))
                    ff=file
        return L[0],ff

# if __name__ == "__main__":
ftpclient = FTPClient()
img_path,img_name=ftpclient.get_imge()
print(img_name)
