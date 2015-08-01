import time
import os
import commands
import basiccommands as base

def checkCreds(username,password):
	userfile = open(os.getenv('HOME')+"/.zerved/accounts",'r')
	credlist = userfile.read().splitlines()
	if(username+'|'+password in credlist):
		return True
	else:
		return False



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
							output = '<h1>Welcome. Enjoy your premium <a href="content">membership.</a></h1>'
					else:
						output = 'You are not logged in. You can log in <a href="login.html">here</a>. If you do not have an account or can not remember the password feel free to use the guest account.'
					commands.connect(name,name+'_cat')
					base.chat(None,name,output)
			elif event['type'] == 'question':
				1
	time.sleep(1)

