# coding=utf-8

import socket

HOST='127.0.0.1'
PORT=3434

s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Connect %s:%d OK" % (HOST,PORT))
data=s.recv(2048)
print("Received: "+data)
s.close()