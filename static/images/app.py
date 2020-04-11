from flask import Flask
import urllib.request
import json

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	# urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
#   	return 'Index Page'

# @app.route('/hello')
# def hello():
#   return 'Hello, greetings from different endpoint'

# #adding variables
# @app.route('/user/<username>')
# def show_user(username):
#   #returns the username
#   return 'Username: %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#   #returns the post, the post_id should be an int
#   return str(post_id)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

with open('images.json') as file:
	data = json.loads(file.read())
	for obj in data:
		n = obj["id"] + ".jpg"
		url = obj["url"]
		print('download', n, url)

		# urllib.request.urlretrieve("type URL here", "path/file_name")
		urllib.request.urlretrieve(url, n)