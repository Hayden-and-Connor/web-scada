from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	data = request.args.get('data')
	return f'Hello World {data}'

@app.route('/another')
def another():
	return 'test'
