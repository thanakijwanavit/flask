#!/usr/bin/env python3
from flask import Flask
import turnonlight, requests
from flask_ask import Ask, statement
app = Flask(__name__)
ask = Ask(app, '/')

rootpage = '''
<h1>%s</h1>
<form>
  <input type="submit" formaction="/lighton" value="lighton">  
  <input type="submit" formaction="/lightoff" value="lightoff">
</form>
'''

returntopage = '''
<h1>%s</h1>
<form>
  <input type="submit" formaction="/lighton" value="lighton">
  <input type="submit" formaction="/lightoff" value="lightoff">
  <input type="submit" formaction="/" value="back">
</form>

'''




@app.route("/")
def hello():
	lightstatus = turnonlight.status()
	return rootpage % lightstatus

@app.route("/light")
def lightstatus():
	return 'light is on'

@app.route("/lightoff")
def lightoff():
	value =turnonlight.off()
	lightstatus = turnonlight.status()
	return returntopage % lightstatus

@app.route("/lighton")
def lighton():
	value =turnonlight.on()
	lightstatus = turnonlight.status()
	return returntopage % lightstatus

@ask.launch 
@ask.intent("LightOn") 
def on(): 
	value =turnonlight.on()
#	lightstatus = turnonlight.status()
	return statement(value) 
@ask.intent("LightOff") 
def off(): 
	value =turnonlight.off()
#	lightstatus = turnonlight.status()
	return statement(value)
@ask.intent("LightStatus")
def status():
	lightstatus = turnonlight.status()
	return statement(lightstatus)
