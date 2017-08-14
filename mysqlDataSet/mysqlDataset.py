
#! encoding=utf-8

import dataset

def  connectMySql():

	db = dataset.connect('mysql://XYJMobile:123456@localhost/XYJMobile')

	result = db.query('SELECT playerId, playerName  FROM t_player_data WHERE playerLevel > 60')

	for row in result:
		print(row['playerId'], row['name'])



connectMySql()