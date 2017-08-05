#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket

class client:

	def testsend(self):
	
		s = socket.socket()

		host = socket.gethostname()

		port = 12345

		s.connect((host,port))

		print s.recv(1024)

		num = s.send('like')

		if num > 0:
			print "send ok"

		s.close()