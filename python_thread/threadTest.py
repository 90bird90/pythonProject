# encoding: utf-8

import threading
import time
# test thread

exitFlag = 0

class  ThreadTest(threading.Thread):

	def __init__(self,threadId,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadId
		self.name = name
		self.counter = counter


	def run(self):

		print "start :", self.name
		print_context(self.name,self.counter,5)
		print "exit :", self.name



def print_context(name,delay, counter):
	if exitFlag:
		threading.Thread.exit()
	time.sleep(delay)
	print "%s: %s" % (name, time.ctime(time.time()))
	counter -= 1


thread1 = ThreadTest(1,"thread1",5)
thread2 = ThreadTest(2,"thread2",10)


thread1.start()
thread2.start()


# WHAT EVER

print "Exiting Main Thread"





