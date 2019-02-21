const socket = io()

socket.on('connect', function(){
	socket.emit('request')
})

// const connect = async function(){

// 	const socket = await Utils.connect()

// 	socket.on('data', function(data){
// 		console.log(data)
// 	})

// 	socket.emit('request')
// }

// window.onload = () => connect()