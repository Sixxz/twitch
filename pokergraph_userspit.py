#!/usr/bin/python3

import requests
import fileinput
from influxdb.influxdb08 import InfluxDBClient
import ssl


clientid = 'bgpmqt0ei7713q8qy4ys70p448ni8q'
clientsecret = '549n7s4y3k75oh45g8cxxx9hnx6z4sv'

def connect_to():
        url = 'https://api.twitch.tv/kraken/streams?limit=50'
        return url

def twitch_parse(data):
	for item in data['streams']: #check the json responce for the item details
		twitch_user = item['channel']['display_name']
		influxdb_name = "twitch.user."+twitch_user+".current_view"
		current_viewer = item['viewers']
		json_body = [{"points":[[current_viewer]],"name":influxdb_name,"columns":["value"]}]
		db = InfluxDBClient('74.82.3.100', 8086, 'twitch_graphing', 'twitch_graph_user', 'twitchgraph')
		db.write_points(json_body)

def submit_url(url):
	response = requests.get(url)
	response.text
	data = response.json()
	twitch_parse(data)
        
url = connect_to()
twitch_data = submit_url(url)
