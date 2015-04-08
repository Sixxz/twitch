import requests
import ssl

def connect_to():
        url = 'https://api.twitch.tv/kraken/search/streams?query=Poker&live=true'
        return url

def submit_url(url):
        response = requests.get(url)
        response.text
        data = response.json()
	print(data)

url = connect_to()
twitch_data = submit_url(url)
