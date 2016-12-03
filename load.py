#!/usr/bin/env python
import datetime
import pickle
import socket

def run():
	h,p="192.168.137.10",18000
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((h,p))
	s.send("hi")
	s.close()
run()	

f=open("log.py","r+")
host=pickle.load(f)
for h,m in host.items():
	if len(m) != 0:
		oldtime = m[-1][0]
		
		differ=(datetime.datetime.now()-oldtime).seconds
		if differ>30:
			print "no data received from %s for %s" % (h,differ)
		else:
			print h,differ
	else:
		print "client %s is down" % (h)





