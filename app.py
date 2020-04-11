from flask import Flask, render_template
import urllib.request
import json
from os import listdir

app = Flask(__name__)

@app.route('/')
def index():
  	return render_template("index.html", images=fetchImageList())

@app.route('/image/<string:name>')
def fetchImageByName(name):
  	return app.send_static_file('images/' + name + '.jpg')

@app.route('/static/<string:name>')
def sendStatic(name):
  	return app.send_static_file(name)

def fetchImageList():
	return [i for i in listdir('static/images') if i.endswith('.jpg')]