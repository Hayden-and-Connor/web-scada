from flask import Flask
from flask import request, send_from_directory

from flask_socketio import SocketIO

import asyncio

import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Disabling these settings lets us run flask in
# a separate thread
app.use_reloader = False
app.debug = False

# Lets flask be externally visible
app.host = '0.0.0.0'

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
	socketio.emit('data', { 'Current': { 'value': 10, 'unit': 'A' }})


from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

import time

ee = EventEmitter()

@ee.on('data')
def handle_data():
    socketio.emit('data', {
        'Temperature': {
            'value': 45,
            'units': 'deg C'
        }
    })

@ee.on('event')
def event_handler():
	print('BANG BANG')

@ee.on('data_new')
def broadcast_data(name, val, ts):
	socketio.emit('data_new', {'name': name, 'val': val, 'ts': ts})

@ee.on('data_new')
def save_data(name, val, ts):
	conn = create_connection("mydata.db")
	with conn:
		create_data(conn, (name, val, ts))

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_data(conn, data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO data(name, value, timestamp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

async def mock_can():
    while True:
        await asyncio.sleep(1)
        ee.emit('data_new', 'mysensor', '10', '5.02')

import threading

async def mock_data():
    
    while True:
        ee.emit('data')
        await asyncio.sleep(1)

if __name__ == "__main__":
    # Threaded = true????
    threading.Thread(target=socketio.run, args=[app, "0.0.0.0"]).start()
    # ee.emit('data_new', 'mysensor', '10', '5.02')
    asyncio.run(mock_data())

