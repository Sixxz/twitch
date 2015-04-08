#!/usr/bin/python3

import requests
import fileinput
import mysql.connector
import ssl

#db = MySQLdb.connect("localhost","pokergraph","pokergraph","pokergraph")

clientid = 'bgpmqt0ei7713q8qy4ys70p448ni8q'
clientsecret = '549n7s4y3k75oh45g8cxxx9hnx6z4sv'

def connect_to():
        url = 'https://api.twitch.tv/kraken/search/streams?query=Poker&live=true'
        return url

def mysql_insert(sql):
	db = mysql.connector.connect(host='localhost',user='pokergraph',password='pokergraph',database='pokergraph')
	cursor = db.cursor()
	cursor.execute(sql)
	db.commit()
	#results = cursor.fetchall()
	db.close

def mysql_select(sql):
	db = mysql.connector.connect(host='localhost',user='pokergraph',password='pokergraph',database='pokergraph')
	cursor = db.cursor()
	cursor.execute(sql)
	results = cursor.fetchall()
	if not cursor.rowcount: 
		db.close
		return "Error"
	else:
		db.close
		return results[0][0]

def twitch_parse(data):
	for item in data['streams']: #check the json responce for the item details
		game_type = item['game']
		twitch_user = item['channel']['display_name']
		current_viewer_count = item['viewers']
		steam_id = item['_id']
		current_favorites = item['channel']['followers']
		subscriber_id = subscriber_process(twitch_user)
		sql = ("INSERT INTO steam_info" "(user_id, steam_id, current_viewers, current_favorites, game)" "VALUES ('%s', '%s', '%s', '%s', '%s' )") % (subscriber_id, steam_id, current_viewer_count, current_favorites, game_type) 
		mysql_insert(sql)

def subscriber_process(twitch_user):
	sql = ("SELECT user_id FROM twitch_user" " WHERE username = '%s' ") % twitch_user #Query the mysql database for the username
	result = mysql_select(sql)
	if result == "Error": #if we don't find the username, we should add the username into the database for next time
		sql_add = ("INSERT INTO twitch_user" "(user_id, username, user_create, user_update)" "VALUES (null,'%s',CURDATE(),CURDATE())") % twitch_user
		mysql_insert(sql_add)
		#at this point we aren't going to care if we return error, this is bad
		new_userid = mysql_select(sql)
		return new_userid
	else:
		return result
	

def submit_url(url):
	response = requests.get(url)
	response.text
	data = response.json()
	twitch_parse(data)
        
	
#def stream_count(user_id, current_viewer_count, stream_id, current_favourites):
 #       insert into database on new line


url = connect_to()

twitch_data = submit_url(url)

