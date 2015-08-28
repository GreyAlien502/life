import math
import time
import os
import json
import urllib

import commands
import basiccommands as base
import zervecommands as zervcom


def send(destination,content):
	block_size = 2300
	checkconnection=False
	if len(content) < block_size:
		base.chat(destination,'0'+content,'')
	else:
		blocked_size = block_size*math.floor(len(content)/block_size)
		lecian = [content[i:i+block_size] for i in range(block_size,len(content)-block_size,block_size)]
		
		base.chat(destination,'1'+content[:block_size],'')
		for lecian_item in lecian:
			base.chat(None,destination,'1'+lecian_item)
		base.chat(destination,'0'+content[blocked_size:],'')


def process(content):
	print(event)

	sendback = content['sendback']
	username = content['username']
	password = content['password']
	command  = content['command' ]

	if (zervcom.checkCreds(username,password)):
		if command == 'login':
			output = zervcom.login(content)
		if command == 'home':
			output = zervcom.home(content)
		if command == 'posts':
			output = zervcom.posts(content)
		if command == 'post':
			output = zervcom.post(content)
		if command == 'comments':
			output = zervcom.comments(content)
		if command == 'comment':
			output = zervcom.comment(content)
	else:
		output = 'You have not entered a correct password. You can log in <a href="login.html">here</a>. If you do not have an account or can not remember the password feel free to use the guest account.'
	send(sendback,json.dumps(output))

hat = "zerving_hat"
while True:
	response = base.keep(hat)
	if 'events' in response:
		for event in response['events']:
			if event['type'] == 'disconnect':
				process(json.loads(event['from']))
