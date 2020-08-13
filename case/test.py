__author__ = 'Administrator'

import datetime
import subprocess


t1 = datetime.datetime.now().strftime("%Y%m%d")
print(t1)


file_out = subprocess.Popen('ping 192.168.102.1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while True:
    line = file_out.stdout.readline().strip().decode("gbk")
    print("line:"+line)
    if subprocess.Popen.poll(file_out)==0:
        break