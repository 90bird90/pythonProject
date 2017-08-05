
from test4 import test4
from test5 import test5

class test3(test4,test5):
	count = 3
	def __init__(self,count):
		self.count = count;
		
	
	def __del__(self):
		print "del", self.__class__.__name__
		
	def prt(self):
		#printf
		print(self)
		print(self.__class__)

