
class test6:

	def __init__(self,count):
		self.count = count;
		
	
	def __del__(self):
		print "del", self.__class__.__name__
		
	def prt(self):
		#printf
		print(self)
		print(self.__class__)
	
	def test5(self):
		print "test6"
		
	def __privateMathod(self):
		print "test6 private method"
		
	def _mthod(self):
		self.__privateMathod();

