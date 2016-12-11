import time
import math
import json
import urllib.request
import urllib.error

import basiccommands as base

def send(destination,content):
	block_size = 2300
	checkconnection=False
	if len(content) < block_size:
		base.chat(destination,'0'+content)
	else:
		blocked_size = block_size*math.floor(len(content)/block_size)
		lecian = [content[i:i+block_size] for i in range(block_size,len(content)-block_size,block_size)]
		
		base.chat(destination,'1'+content[:block_size])
		for lecian_item in lecian:
			base.chat(destination,'1'+lecian_item)
		base.chat(destination,'0'+content[blocked_size:])

def proxy(address, url, delay=1):
	while True:
		try:
			response = base.keep(address)
		except urllib.error.HTTPError:
			response = []
		if 'events' in response:
				for event in response['events']:
					message = json.loads(event['from'])
					send(
						message['sendback'],
						urllib.request.urlopen(url+message['data']).read().decode("UTF-8")
					)

	time.sleep(delay)
