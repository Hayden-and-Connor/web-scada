const express = require('express')
const app = express()
const http = require('http').Server(app)
const expressWs = require('express-ws')(app)

const path = require("path")
const events = require("events")

const interface = new events()

// console.log(ws)

// Disable Cross-Origin resource restrictions
const cors = require('cors')
app.use(cors())

const bodyParser = require('body-parser')
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


let subscribers = []

app.use('/', express.static('client'))
app.get('/', function(req, res){
	res.sendFile('client/index.html')
})

app.get('/data', function(req, res){
	interface.emit('data', { "y": 45 })

	res.send('ok')
})

app.ws('/subscribe', function(ws, req){
	const send = function(data){
		ws.send('data', data)
	}

	interface.on('data', send)
	ws.on('close', () => interface.removeListener('data', send))	
})

app.listen(80)