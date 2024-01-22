# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
对于40W的功率，10lg(40W/1mw)=10lg(40000)=10(4+lg4)=46dBm
dBm-dBm = dB
"""

#import numpy as np
import matplotlib.pyplot as plt
#import pickle
import scapy.all as scapy

# pcaps = scapy.rdpcap("./data/walkclose.pcap")
# pcaps = scapy.rdpcap("./data/empty.pcap")
pcaps = scapy.rdpcap('E:\matlab\data\location\B202\20230224\YI_tr1.pcap')
i = 0
j = 0
dat_len = [0]*2001
dat_tim = [0]*2001
# dat_SNR = [0]*1001
while i < 2001:
    if pcaps[i].subtype == 8 and len(pcaps[i].data) != 1080:                #只计算数据类型为数据帧
        dat_len[j] = len(pcaps[i].data)         #计算数据包长度
        dat_tim[j] = pcaps[i].time-pcaps[0].time    #计算数据包时间
        # dat_SNR[i] = pcaps[i].dBm_AntSignal-pcaps[i].dBm_AntNoise   #计算信噪比dB
        # if dat_SNR[i] < 0:
            # dat_SNR[i] = dat_SNR[i] + 256
        i = i+1
        j = j+1
        # print(i)
    else:
        i = i+1

# plt.plot(dat_tim)
# plt.plot(dat_tim,dat_SNR)
# np.savetxt("datatest.txt",dat_len)


# with open("length.txt", "wb") as f:     #以二进制把list写入一个文件
#     pickle.dump(dat_len,f)
    
# with open("time.txt", "wb") as fp:      #以二进制把list类型写入一个文件
#     pickle.dump(dat_tim,fp)

# with open("lenth.txt", "rb") as f:      #以二进制把文件读取为list类型
#     b = pickle.load(f) 

#计算比特率，固定时间内发送的字节数
# m = 1
# n = 0
# low = 0
# rate = [0]*10000
# temp = dat_len[0]
# while m<6001:
#     if dat_tim[m] == 0:
#         m = m+1
#         continue
    
#     if dat_tim[m]-dat_tim[low] > 0.2:
#         rate[n] = dat_len[m]+temp
#         temp = 0
#         low = m
#         n = n+1
#         m = m+1
#     else:
#         temp = temp+dat_len[m]
#         m = m+1
        
# plt.plot(rate[1:100])






























