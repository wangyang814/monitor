#!/usr/bin/env python
import socket
host,port="192.168.137.10",18000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
s.send("up")
s.close()
