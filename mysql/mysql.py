#!/usr/bin/python
#-*- coding: UTF-8 -*-

import MySQLdb
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

class mysqltest:

	def test1(self):
		# 打开数据库连接
		db = MySQLdb.connect(host = "127.0.0.1",user ="root",passwd ="123456",db ="xyjmobile",charset="utf8")

		# 使用cursor()方法获取操作游标 
		cursor = db.cursor()

		
		sql = "select * from t_player_data where playerLevel > '%d'" % (20)
		# 使用execute方法执行SQL语句
		cursor.execute(sql)

		fo = open("text.txt","w+")
		
		# 使用 fetchone() 方法获取一条数据库。
		data = cursor.fetchall()
		index = 0;
		for row in data:

			#context = str(index) + ' ' + str(row[0]) +' ' + str(row[1])  + ' ' + str(row[2]) + ' ' + str(row[3]) + '\n'
			#fo.write(context.decode("utf-8"))
			fo.write(str(row).decode("utf-8") + '\n')
			index += 1

		#print "Database version : %s " % data

		# 关闭数据库连接
		db.close()





	