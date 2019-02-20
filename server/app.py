from flask import Flask
from flask import request, send_from_directory

from flask_socketio import SocketIO

import asyncio

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

@socketio.on('request')
def handle_request():
	print('data requested')
	socketio.emit('data', { 'Current': { 'value': 10, 'unit': 'A' }, 'key2': 200 })

app.run()
socketio.run(app)