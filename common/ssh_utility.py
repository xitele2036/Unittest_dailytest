# -*- coding: utf-8 -*-
__author__ = 'Jason Liu'

import paramiko
import time

# def Singleton(cls):
#     _instance = {}
#
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]
#
#     return _singleton
#
# @Singleton
class SSHUtility:

    # 初始化
    def __init__(self,usernames,passwords,hostnames):
        self.usernames = usernames
        self.passwords = passwords
        self.hostnames = hostnames
        self.s = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 建立SSH连接
    def connect(self):
        self.s.connect(self.hostnames,22,self.usernames,self.passwords)

    # 发送命令并返回原始结果
    def send1(self,comm):
        stdin, stdout, stderr = self.s.exec_command(comm.encode())
        line = stdout.read()
        # print(line)
        return line.decode()

    # 发送命令返回经过解析后的结果，不带result:
    def send2(self,comm):
        stdin, stdout, stderr = self.s.exec_command(comm.encode())
        line = stdout.read()
        # print(line)
        return line[7:].decode()

    # 发送命令等待一段时间才会有返回原始结果
    def send3(self,comm,timeout):
        stdin, stdout, stderr = self.s.exec_command(comm.encode())
        time.sleep(timeout)
        line = stdout.read()
        # print(line)
        return line.decode()

    # 关闭SSH连接
    def close(self):
        self.s.close()









