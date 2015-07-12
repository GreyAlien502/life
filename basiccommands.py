import urllib.request
import json

def __get(options):
	return json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?'+urllib.parse.urlencode(options)).read().decode('UTF-8'))

def login(ID=None):
	options = {'cmd':'login'}
	if ID != None:
		options.update({'id':ID})
	return __get(options)
def keep(ID=None):
	options = {'cmd':'keep'}
	if ID != None:
		options.update({'id':ID})
	return __get(options)
def disconnect(ID='',to=''):
	options = {'cmd':'disconnect'}
	if ID != None:
		options.update({'id':ID})
	if to != None:
		options.update({'to':to})
	return __get(options)
def chat(ID=None,to=None,message=None):
	options = {'cmd':'chat'}
	if ID != None:
		options.update({'id':ID})
	if to != None:
		options.update({'to':to})
	if message != None:
		options.update({'content':message})
	return __get(options)
	
