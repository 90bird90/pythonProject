
#! encoding=utf-8

import dataset

SELECT_STR = 'SELECT playerId,playerName,playerLevel  FROM t_player_data WHERE playerLevel > 60'
UPDATE_STR = 'UPDATE t_player_data SET professionType = 5 WHERE playerLevel > 60'


def connectMySql(type,queryStr):

	try:
		db = dataset.connect('mysql://XYJMobile:123456@127.0.0.1/XYJMobile')
	except:
		print "db connect exception"


	try:
		result = db.query(queryStr)
		if type == 1 :

			for row in result:
				print(row['playerId'], str(row['playerName']).decode("UTF-8"),row['playerLevel'])
	except:
		print "db query exception"



def connectMysql2(tabName,type,queryStr=''):
	try:
		db = dataset.connect('mysql://XYJMobile:123456@127.0.0.1/XYJMobile')
	except:
		print "db connect exception"

	try:
		table = db[tabName]
	except:
		print "table exception",tabName


	if type == 1:

		result = table.find(professionType=5)
		for row in result:
			print(row['playerId'], row['professionType'], row['playerLevel'])

	elif type == 2:
		table.update(dict(playerLevel=61, professionType=6), ['playerLevel'])

	elif type == 3:
		table.insert(dict(index=2,playerId=123456, playerName='John Doe', playerLevel=80))

	else:
		table.insert(dict(index=1, name='John Doe', age=46, country='China'))


connectMysql2('t_test',3)