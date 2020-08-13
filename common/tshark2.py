#-*-coding:utf8-*-

import os,sys
import time
from scapy.all import *

def parse_ip():
    pcaps = rdpcap(r"C:\Program Files\Wireshark\2.pcap")
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

def parse_tcp():
    pcaps = rdpcap(r"C:\Program Files\Wireshark\2.pcap")
    for data in pcaps:
        if 'TCP' in data:
            s = repr(data)
            print(s)
            sport = data['TCP'].sport
            dport = data['TCP'].dport
            print(sport)
            print(dport)
        return sport,dport

def parse_udp():
    pcaps = rdpcap(r"C:\Program Files\Wireshark\2.pcap")
    for data in pcaps:
        if 'TCP' in data:
            s = repr(data)
            print(s)
            sport = data['TCP'].sport
            dport = data['TCP'].dport
            print(sport)
            print(dport)
        return sport,dport

def parse_1q():
    pcaps = rdpcap(r"C:\Program Files\Wireshark\11111.pcap")
    for data in pcaps:
        # print(data)
        if 'Dot1Q' in data:
            # print(data.show())
            s = repr(data)
            print(data['Dot1Q'].vlan)
            # s2=repr(data['Dot1Q'].payload.show())
            print(data['Dot1Q'].payload.name)
            if data['Dot1Q'].payload.name == "802.1Q":
                print(data['Dot1Q'].payload.vlan)

if __name__ == '__main__':
    ver,src,dst = parse_ip()
    print(ver,src,dst)
