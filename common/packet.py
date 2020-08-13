__author__ = 'Administrator'

import os,time
import subprocess
from scapy.all import *

class Packet( object):

    def __init__(self):
        self.tshark_path = "C:\\Program Files\\Wireshark\\"
        self.dir =os.getcwd()

    #利用xcap发包
    def sendPacket(self,type,times,speed):
        base_path = os.path.abspath(".")
        xcap_path = base_path + "\\xcap\\txpacket.exe"
        pcap_path = base_path + "\\xcap\\bbbb.pcap"
        batch_cmd= xcap_path +" -n 0 -f "+ pcap_path+" -p 0 -t "+str(times)+" -s "+str(speed)
        # print(xcap_path)
        # print(batch_cmd)
        # os.system(batch_cmd)
        subprocess.Popen(batch_cmd,shell=True)
        self.captureAllPacket(30)
        # self.capturePacket(30,"src host 192.168.102.1","sss.pcap")
        time.sleep(times)

        # file_out = subprocess.Popen(batch_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def captureAllPacket(self,times):
        os.chdir(self.tshark_path)
        capture_cmd = "tshark.exe -i 3" +" -a duration:"+str(times)+" -w test.pcap"
        print(capture_cmd)
        # os.system(capture_cmd)
        subprocess.Popen(capture_cmd,shell=True)
        os.chdir(self.dir)

    """
    @times:抓包时长
    @filter:过滤规则
    常见的几种过滤规则
    -f "ip.src==192.168.102.1" 过滤原地址为192.168.102.1的报文
    @output：抓取的包保存为一个文件
    """
    #tshark.exe -i 4 -a duration:30 -w test.pcap
    #tshark.exe -i 4 -a duration:300 -f "src host 192.168.102.1" -w test3.pcap

    def capturePacket(self,times,filter):
        os.chdir(self.tshark_path)
        capture_cmd = "tshark.exe -i 3" +" -a duration:"+str(times)+" -f "+"\""+filter+"\""+" -w test.pcap"
        print(capture_cmd)
        # os.system(capture_cmd)
        subprocess.Popen(capture_cmd,shell=True)
        os.chdir(self.dir)

    def parse_ip(self):
        pcaps = rdpcap(r"C:\Program Files\Wireshark\test.pcap")
        for data in pcaps:
            if 'IP' in data:
                # print(data.show())
                # s = repr(data)
                # print(s)
                version = data['IP'].version
                src = data['IP'].src
                dst = data['IP'].dst
                # print(version)
                # print(src)
                # print(dst)
            return version,src,dst

    def parse_tcp(self):
        pcaps = rdpcap(r"C:\Program Files\Wireshark\test.pcap")
        for data in pcaps:
            if 'TCP' in data:
                s = repr(data)
                print(s)
                sport = data['TCP'].sport
                dport = data['TCP'].dport
                print(sport)
                print(dport)
            return sport,dport

    def parse_udp(self):
        pcaps = rdpcap(r"C:\Program Files\Wireshark\test.pcap")
        for data in pcaps:
            if 'TCP' in data:
                s = repr(data)
                # print(s)
                sport = data['TCP'].sport
                dport = data['TCP'].dport
                # print(sport)
                # print(dport)
            return sport,dport

    def parse_1q(self):
        cvlan = 0
        pcaps = rdpcap(r"C:\Program Files\Wireshark\test.pcap")
        for data in pcaps:
            # print(data)
            if 'Dot1Q' in data:
                # print(data.show())
                s = repr(data)
                # print(data['Dot1Q'].vlan)
                cvlan = data['Dot1Q'].vlan
                # s2=repr(data['Dot1Q'].payload.show())
                # print(data['Dot1Q'].payload.name)
                # if data['Dot1Q'].payload.name == "802.1Q":
                #     print(data['Dot1Q'].payload.vlan)
        return cvlan

    def parse_qinq(self):
        cvlan = 0
        svlan = 0
        pcaps = rdpcap(r"C:\Program Files\Wireshark\test.pcap")
        for data in pcaps:
            # print(data)
            if 'Dot1Q' in data:
                # print(data.show())
                s = repr(data)
                print(data['Dot1Q'].vlan)
                cvlan = data['Dot1Q'].vlan
                # s2=repr(data['Dot1Q'].payload.show())
                print(data['Dot1Q'].payload.name)
                if data['Dot1Q'].payload.name == "802.1Q":
                    print(data['Dot1Q'].payload.vlan)
                    svlan = data['Dot1Q'].payload.vlan
        return cvlan ,svlan
if __name__ == "__main__":
    packet = Packet()
    packet.sendPacket(1,10,1)
    ff='-Y "ip.src==192.168.102.1"'
    # packet.capturePacket(30,"src host 192.168.102.1","sss.pcap")
    cvlan =packet.parse_1q()
    print(cvlan)
    # print(os.getcwd())

