import math
import time
import os
import json
import urllib

import commands
import basiccommands as base
import zervecommands as zervcom


def send(destination,content):
	def tryQuickChat(destination,message):
		base.chat(destination+"_cat",destination,message)
		base.chat(destination,destination+'_cat','Look at me NOW!')
		if(commands.getResponse(destination+'_cat')['events'][-1]['type']=='disconnect'):
			print('imperfiect')
			commands.connect(destination+'_cat',sendback)
			base.chat(destination+'_cat',destination,message)
	block_size = 2300
	checkconnection=False
	if len(content) < block_size:
		tryQuickChat(destination,'0'+content)
	else:
		blocked_size = block_size*math.floor(len(content)/block_size)
		lecian = [content[i:i+block_size] for i in range(block_size,len(content)-block_size,block_size)]
		tryQuickChat(destination,'1'+content[:block_size])
		for lecian_item in lecian:
			base.chat(None,destination,'1'+lecian_item)
		base.chat(None,destination,'0'+content[blocked_size:])



cat = "zerving_cat"
hat = "zerving_hat"
commands.connect(cat,hat)
while True:
	base.chat(hat,cat,"Look at me NOW!")
	base.keep(cat)
	response = base.keep(hat)
	if 'events' in response:
		for event in response['events']:
			print(event)
			if event['type'] == 'connected':
				1
			elif event['type'] == 'disconnect':
				commands.connect(cat,hat)
			elif event['type'] == 'msg':
				if event['from'] == None:
					content = json.loads(event['content'])

					sendback = content['sendback']
					username = content['username']
					password = content['password']
					command  = content['command' ]
					data     = content['data'    ]

					if (zervcom.checkCreds(username,password)):
						if command == 'login':
							output = zervcom.login(content)
						if command == 'home':
							output = zervcom.home(content)
						if command == 'posts':
							output = zervcom.posts(content)
						if command == 'post':
							output = zervcom.post(content)
					else:
						output = 'You have not entered a correct password. You can log in <a href="login.html">here</a>. If you do not have an account or can not remember the password feel free to use the guest account.'
					send(sendback,json.dumps(output))
				else:
					commands.connect(cat,hat)
			elif event['type'] == 'question':
				1
	#time.sleep(.05)

