
class test4:

	def __init__(self,count):
		self.count = count;
		
	
	def __del__(self):
		print "del", self.__class__.__name__
		
	def prt(self):
		#printf
		print(self)
		print(self.__class__)
	
	def test4(self):
		print "test4"

