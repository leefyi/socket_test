# coding=utf-8

import socket

HOST='0.0.0.0'
PORT=3434

# AF_INET-IPV4  SOCK_DGRAM-UDP
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    data,addr=s.recvfrom(2048)
    print(addr)
    # addr包含IP和端口，为动态端口号
    # 相同的程序每次运行，OS都会分配一个端口号，不允许相同
    print("Recevied: %r from %s" %(data,str(addr)))

s.close()