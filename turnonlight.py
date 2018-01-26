#!/usr/bin/env python3
import requests


def on():
	r=requests.get('http://10.0.1.169/turnledon')
	return r.text

def off():
	r=requests.get('http://10.0.1.169/turnledoff')
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
