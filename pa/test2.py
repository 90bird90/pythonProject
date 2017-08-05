
def test2():

	try:
		fo = open("text.txt","a")
		print "file name : ",fo.name
	
		context = fo.read()
		print "context :",context
	
		str = raw_input("input: ")
		fo.write(str);
		fo.flush()
		fo.close()
	except IOError:
		print "error"
	else:
		print "end"