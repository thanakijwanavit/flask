#!/usr/bin/env python3
from flask import Flask
import turnonlight, requests

app = Flask(__name__)
rootpage = '''
<form>
  <input type="submit" formaction="/lighton" value="lighton">  
  <input type="submit" formaction="/lightoff" value="lightoff">
</form>
'''

returntopage = '''
<form>
  <input type="submit" formaction="/lighton" value="lighton">
  <input type="submit" formaction="/lightoff" value="lightoff">
  <input type="submit" formaction="/" value="back">
</form>

'''



@app.route("/")
def hello():
	return rootpage

@app.route("/light")
def lightstatus():
	return 'light is on'

@app.route("/lightoff")
def lightoff():
	value =turnonlight.off()
	return returntopage

@app.route("/lighton")
def lighton():
	value =turnonlight.on()
	return returntopage

