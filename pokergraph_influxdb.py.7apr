#!/usr/bin/python3

import requests
import fileinput
from influxdb.influxdb08 import InfluxDBClient
import ssl


clientid = 'bgpmqt0ei7713q8qy4ys70p448ni8q'
clientsecret = '549n7s4y3k75oh45g8cxxx9hnx6z4sv'

def connect_to():
        url = 'https://api.twitch.tv/kraken/search/streams?query=Poker&live=true'
        return url

def twitch_parse(data):
	for item in data['streams']: #check the json responce for the item details
		twitch_game_type = item['game']
		twitch_user = item['channel']['display_name']
		current_viewer = item['viewers']
		stream = item['_id']
		current_fav = item['channel']['followers']
		print(twitch_game_type, twitch_user, current_viewer, stream, current_fav)
		json_body = [{"points":[[twitch_game_type,twitch_user,current_viewer,stream,current_fav]],"name":"twitch_stream_counting","columns":["games_type","twitch_username","current_viewer_count","steam_id","current_favorites"]}]
		db = InfluxDBClient('74.82.3.100', 8086, 'poker_user', 'pokergraph', 'pokergraph')
		db.write_points(json_body)

def submit_url(url):
	response = requests.get(url)
	response.text
	data = response.json()
	twitch_parse(data)
        
url = connect_to()
twitch_data = submit_url(url)
