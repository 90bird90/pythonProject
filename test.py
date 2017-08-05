
#-*- coding:utf-8 -*-
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
from package_pa.text import test
from pa.test1 import test1
from pa.test2 import test2
from pa.test3 import test3
from pa.test4 import test4
from pa.test5 import test5
from pa.test6 import *
from mysql.mysql import mysqltest
from sockettest.server import server
 
#runoob1()
#runoob2()
#test()
#test1()
#test2()
#t= test6(3)
#print "is :",isinstance(t,test3)
#t._mthod()

#t._test6__privateMathod()

'''t.age = 7
print(t.count)
print(t.age)
print(getattr(t,'count'))
print(hasattr(t,'count'))
print(hasattr(t,'age'))

t=test3(8)
print "Employee.__doc__:", test3.__doc__
print "Employee.__name__:", test3.__name__
print "Employee.__module__:", test3.__module__
print "Employee.__bases__:", test3.__bases__
print "Employee.__dict__:", test3.__dict__
print "\n"'''

t = mysqltest()
t.test1()

#t= server()
#t.testconnect()