from flask import Flask
from flask import request, send_from_directory

from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
	return send_from_directory('../client', 'index.html')

@app.route('/client/<path:path>')
def public(path):
	return send_from_directory('../client', path)

@socketio.on('connect')
def handle_connect():
	print('connected')

app.run()
# socketio.run(app)