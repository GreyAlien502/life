import math
import time
import os
import json
import urllib

import commands
import basiccommands as base


def checkCreds(username,password):
	userfile = open(os.getenv('HOME')+"/.zerved/accounts",'r')
	credlist = userfile.read().splitlines()
	if(username+'|'+password in credlist):
		return True
	else:
		return False

def send(destination,content):
	if len(content) < 8000:
		base.chat(None,destination,'0'+content)
	else:
		block_size = 2300
		blocked_size = block_size*math.floor(len(content)/block_size)
		lecian = [content[i:i+block_size] for i in range(0,len(content)-block_size,block_size)]
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

					if (checkCreds(username,password)):
						if command == 'login':
							output = '<h1>Welcome. Enjoy your premium <a href="content.html">membership.</a></h1>'
						if command == 'home':
							output = '<a href="../index.html">Home</a><br>Hello '+username+'<br><a onclick="posts()">Posts</a> <a onclick="files()">Personal Files</a> <a onclick="logout()">Logout</a> <a onclick="messages"> Messages</a> <a onclick="seeBash()">Bash</a> <a onlick="preferences()">Preferences</a>'
					else:
						output = 'You have not entered a correct password. You can log in <a href="login.html">here</a>. If you do not have an account or can not remember the password feel free to use the guest account.'
					print('connecting')
					commands.connect(sendback,sendback+'_cat')
					print('connected')
					send(sendback,json.dumps(output))
				else:
					commands.connect(cat,hat)
			elif event['type'] == 'question':
				1
	#time.sleep(.05)

