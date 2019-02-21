window.onload = function(){
	const socket = io('http://localhost:5000');
	socket.connect();

	socket.on('another', function(data){
		console.log(data)
	})
}