#!/usr/bin/env python

import SocketServer
import datetime
import pickle
host_status={}
with open("account.py","r+") as f:
	while True:
		line = f.readline().split()
		if len(line) == 0:break
		host_status[line[0]] = []
		 
		
class myclass(SocketServer.BaseRequestHandler):
	def handle(self):
		recv_data=self.request.recv(1024)
		if self.client_address[0] == "192.168.137.10":
			with open("log.py","r+") as f:
				pickle.dump(host_status,f)
				f.close()	 
		if self.client_address[0] in host_status.keys():
			host_status[self.client_address[0]].append((datetime.datetime.now(),recv_data))
		else:
			print "%s is not be monitored" %s (self.client_address[0])
		print "from %s: %s: %s"%(self.client_address,datetime.datetime.now(),recv_data)
		print host_status

if __name__ == "__main__":
	host,port = "",18000
	server = SocketServer.ThreadingTCPServer((host,port),myclass)
	server.serve_forever()

