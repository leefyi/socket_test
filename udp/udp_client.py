# coding=utf-8

import socket

HOST='127.0.0.1'
PORT=3434

s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
data="Hello UDP!"
s.sendto(data,(HOST,PORT))
print("Sent: %r to %s:%d OK" %(data,HOST,PORT))
s.close()