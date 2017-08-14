from jpype import *
import os.path
jarpath = os.path.join(os.path.abspath('.'), 'F:/sample_Py/')
startJVM("C:/Java/jdk1.6.0_10/jre/bin/client/jvm.dll","-ea", "-Djava.class.path=%s" % (jarpath + 'jpypedemo.jar'))
#ubuntu 中startJVM("/home/geek/Android/jdk1.6.0_43/jre/lib/i386/server/libjvm.so","-ea", "-Djava.class.path=%s" % (jarpath + 'XXX.jar'))
JDClass = JClass("jpype.JpypeDemo")
jd = JDClass()
#jd = JPackage("jpype").JpypeDemo() #两种创建jd的方法
jprint = java.lang.System.out.println
jprint(jd.sayHello("waw"))
jprint(jd.calc(2,4))
shutdownJVM()