const Utils = {}

// Establish a connection to the server. Resolve if successful and rejct if not
Utils.connect = function(){
	return new Promise(function(resolve, reject){
		try {
			const socket = io()
			socket.on('connect', () => resolve(socket))
		} catch(err) {
			reject(err)
		}
	})
}

Utils.DomQuery = function(query){
	const nodelist = document.querySelectorAll(query)
	return Array.prototype.slice.call(nodelist)
}