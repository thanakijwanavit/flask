#!/usr/bin/env python3
import requests
import signal
def handler(signum, frame):
	print('timeout')
	raise Exception('time is up')

def on():
	try:
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(5)
		r=requests.get('http://blynk-cloud.com/56827b4bcc60404f842f2775cd1539e7/update/V3?value=1')
		#r.raise_for_status()
		signal.alarm(0)
		return r.text
	except:
		#return "page not found"
		print ('error')
def off():
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(5)
	r=requests.get('http://blynk-cloud.com/56827b4bcc60404f842f2775cd1539e7/update/V3?value=0')
	#r.raise_for_status()
	signal.alarm(0)
	return r.text
def test():
	return 'abc'

'''while True:
	usercommand = input('on or off\n')
	if usercommand == 'on':
		on()
	elif usercommand == 'off':
		off()
	else:
		print('press on or off')
		continue
'''
def status():
	r=requests.get('http://10.0.1.169/lightstatus')
	return r.text
