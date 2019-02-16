const Utils = {}


Utils.websocket = function(url){
	return new Promise(function(resolve, reject){
		const socket = new WebSocket(url)

		socket.onopen = () => resolve(socket)
		socket.onerror = () => reject(socket)
	})
}

window.onload = async function(){
	// const socket = await Utils.websocket('ws://localhost/subscribe')

	// socket.send('message')

	const svg = d3.select('svg')
	const element = document.querySelector('.graph-container')

	console.log(element)

	const width = 1000
	const height = 1000

	const xScale = d3.scaleLinear()
	    .domain([0, 20-1]) // input
	    .range([0, width]); // output

	const yScale = d3.scaleLinear()
	    .domain([0, 1]) // input 
		.range([height, 0]); // output 

	const dataset = d3.range(20).map(elem => ({"y": d3.randomUniform(1)() }))

	dataset.push({"y": d3.randomUniform(1)() })

	// const xAxis = d3.svg.axis()
	// const yAxis = d3.axisRight().scale(xScale)

	// svg.append('g').call(xAxis)
	// svg.append('g').call(yAxis)

	svg.selectAll('.dot')
	.data(dataset).enter()	// for each point in the data-set
	.append('circle')		// append a circle
	.attr('cx', (d, i) => xScale(i))
	.attr('cy', d => yScale(d.y))
	.attr('r', 5)

	const line = d3.line()
		.x((data, index) => xScale(index))
		.y(point => yScale(point.y))
		// .interpolate('linear')

	svg.append('path')
	.attr('d', line(dataset))
	.attr('stroke', 'red')
	.attr('fill', 'none')
}