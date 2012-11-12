import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.test
names = db.names
item = names.find_one()

nickname = {'text': 'chinna1'}

if 'nicknames' not in item.keys():
	item['nicknames'] = []

item['nicknames'].append(nickname)

names.save(item)

print item