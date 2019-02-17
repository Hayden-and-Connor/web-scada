from flask import Flask
from flask import request, send_from_directory

from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)
socketio.run(app)


@app.route('/')
def index():
	return send_from_directory('client', 'index.html')

@app.route('/client/<path:path>')
def public(path):
	return send_from_directory('client', path)

@app.route('/another')
def another():
	socketio.emit('another', {'data': 42})
	return 'test'

@socketio.on('connect')
def handle_connect():
	print('connected')

