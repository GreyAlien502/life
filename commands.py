import basiccommands as base

def getResponse(ID):
	response = {}
	while 'events' not in response:
		response = base.keep(ID)
	return response

def connect(ID1,ID2):
	origin = ''
	while origin != ID2:
		base.login(ID1)
		base.login(ID2)
		connection = False
		while connection == False:
			eventlecian=getResponse(ID1)['events']
			for event in eventlecian:
				if event['type'] == 'connected':
					connection = True
					print(event)
					origin = event['from']

def attend(ID,pause=1):
	while True:
		for event in getResponse(ID)['events']:
			print(event['type']+"\tfrom "+event['from']+"\t@"+event['time']+'\t|'+event['content'])
