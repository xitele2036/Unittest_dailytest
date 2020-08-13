__author__ = 'Administrator'


import subprocess

file_out = subprocess.Popen('ping 192.168.102.1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while True:
    line = file_out.stdout.readline().decode("gbk")
    print(line)
    if subprocess.Popen.poll(file_out)==0:
        break


