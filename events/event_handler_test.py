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

from pyee import EventEmitter

import sqlite3
from sqlite3 import Error

ee = EventEmitter()

@ee.on('event')
def event_handler():
	print('BANG BANG')

@ee.on('data_new'):
def broadcast_data(name, val, ts):
	socketio.emit('data_new', {'name': name, 'val': val, 'ts': ts})

@ee.on('data_new'):
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
    sql = ''' INSERT INTO data(name,val,ts)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

