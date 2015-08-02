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
	def rawChat(to,message):
		print(message)
		options = 'cmd=chat&to='+to+'&content='+message
		return base._get(options,True)
	content=urllib.parse.urlencode({"content":content})[9:]
	if len(content) < 8000:
		chat(None,destination,'0'+content)
	else:
		blocked_size = 5000*math.floor(len(content)/5000)
		lecian = [content[i:i+5000] for i in range(0,len(content),5000)]
		for lecian_item in lecian:
			rawChat(destination,'1'+lecian_item)
		rawChat(destination,'0'+content[blocked_size:])



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
			elif event['type'] == 'disconnected':
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
							output = '<a href="../index.html">Home</a><br>Hello '+username+'. Enjoy the site.<br><input type="button" onclick="messageboard()"><br>'+3000*'(^_^)'
					else:
						output = 'You have not entered a correct password. You can log in <a href="login.html">here</a>. If you do not have an account or can not remember the password feel free to use the guest account.'
					commands.connect(sendback,sendback+'_cat')
					send(sendback,json.dumps(output))
			elif event['type'] == 'question':
				1
	#time.sleep(.05)

