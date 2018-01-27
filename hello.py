#!/usr/bin/env python3
from flask import Flask
import turnonlight, requests

app = Flask(__name__)
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

