#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket

class server:

	def testconnect(self):
		
		s= socket.socket()

		host = socket.gethostname()

		port = 12345

		s.bind((host,port))

		s.listen(5)


		while True:
			c,addr = s.accept()
			print "connect address : ",addr
			c.send('welcome to connect!')
			data,ok = c.recvfrom(1024)
			print "recv ",str(data)
			c.close()
			'''if str == 'like':
				print "recv like"
				break'''

