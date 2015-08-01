import time
import os
import commands
import basiccommands as base

def checkCreds(creds):
	userfile = open(os.getenv('HOME')+"/.zerved/accounts",'r')
	credlist = userfile.read().splitlines()
	if(creds in credlist):
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
			print('e')
			print(event)
			if event['type'] == 'connected':
				1
			elif event['type'] == 'disconnected':
				commands.connect(cat,hat)
			elif event['type'] == 'msg':
				if event['from'] == None:
					name = event['content'].splitlines()[0]
					credentials = event['content'].splitlines()[1]
					command = '\n'.join(event['content'].splitlines()[2:])
					if (checkCreds(credentials)):
						if command == 'login':
							output = '<h1>Welcome. Enjoy your premium membership.</h1>'
					else:
						output = "You don't belong here."
					commands.connect(name,name+'_cat')
					base.chat(None,name,output)
			elif event['type'] == 'question':
				1
	time.sleep(1)

