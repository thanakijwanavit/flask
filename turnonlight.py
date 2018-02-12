#!/usr/bin/env python3
import requests
import signal
import time
def handler(signum, frame):
	print('timeout')
	raise Exception('time is up')

def on():
	try:
		#signal.signal(signal.SIGALRM, handler)
		#signal.alarm(5)
		r=requests.get('''http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/update/V3?value=1''',timeout=5)
		r=requests.get("http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/get/v1",timeout=1)
		#headers = {"Content-Type":"application"}
		#data = {"1"}
		#params = dict()
		#requests.get("http://blynk-cloud.com/56827b4bcc60404f842f2775cd1539e7/update", params=params)
		#url = "http://blynk-cloud.com/56827b4bcc60404f842f2775cd1539e7/update/V3"
		#r=requests.put(url, data=data, headers=headers, timeout=5)
		#r.raise_for_status()
		#signal.alarm(0)
		#r=requests.get('http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/isHardwareConnected', timeout=5)
		lightstatus = status()
		return lightstatus
#		return r.text
	except:
		#return "page not found"
		print ('error')
def off():
	#signal.signal(signal.SIGALRM, handler)
	#signal.alarm(5)
	r=requests.get('http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/update/V3?value=0',timeout=5)
	r=requests.get("http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/get/v1",timeout=1)
	#r.raise_for_status()
	#signal.alarm(0)
	lightstatus = status()
	return  lightstatus
#	return r.text
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
	time.sleep(1)
	r=requests.get("http://188.166.206.43/56827b4bcc60404f842f2775cd1539e7/get/v1",timeout=1)
#	r=requests.get('http://10.0.1.169/lightstatus')
	if r.text=="[\"0\"]":
		lightstatus = 'light is off'
	elif r.text =="[\"255\"]":
		lightstatus = 'light is on'
	else:
		lightstatus = 'error'
	return lightstatus
