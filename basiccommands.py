import urllib.request
import json

def _get(options,timeout=None):
	if timeout != None: output = json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?'+options,                              None,timeout).read().decode('UTF-8'))
	else:          output = json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?'+urllib.parse.urlencode(options)).read().decode('UTF-8'))
#	print(output)
	return output

def login(ID=None):
	options = {'cmd':'login'}
	if ID != None:
		options.update({'id':ID})
	return _get(options)
def keep(ID=None):
	options = {'cmd':'keep'}
	if ID != None:
		options.update({'id':ID})
	return _get(options)
def disconnect(ID='',to=''):
	options = {'cmd':'disconnect'}
	if ID != None:
		options.update({'id':ID})
	if to != None:
		options.update({'to':to})
	return _get(options)
def chat(ID=None,to=None,message=None,timeout=None):
	options = {'cmd':'chat'}
	if ID != None:
		options.update({'id':ID})
	if to != None:
		options.update({'to':to})
	if message != None:
		options.update({'content':message})
	return _get(options,timeout)
	
