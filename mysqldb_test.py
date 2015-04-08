#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","pokergraph","pokergraph","pokergraph")
cursor = db.cursor()
cursor.execute("SELECT user_id FROM twitch_user WHERE username = 'Alexxic'")
data = cursor.fetchone()
print "Database version : %s " % data
db.close()
