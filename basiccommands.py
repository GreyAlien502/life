import urllib.request
import json

def login(ID=''):
	return json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?cmd=login&id='+ID+'&plat=iphone').read().decode('UTF-8'))
def keep(ID=''):
	return json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?cmd=keep&id='+ID+'&plat=iphone').read().decode('UTF-8'))
def disconnect(ID='',to=''):
	return json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?cmd=disconnect&id='+ID+'&to='+to+'&plat=iphone').read().decode('UTF-8'))
def chat(ID='',to='',message=''):
	return json.loads(urllib.request.urlopen('http://ec.androiddown.com/chat/app.php?cmd=chat&id='+ID+'&to='+to+'&content='+message+'&plat=iphone').read().decode('UTF-8'))
