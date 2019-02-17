#d3 example
## A working example of a line graph drawn with D3 using random data

For reference, check client/data.js
or read here:

```javascript
	const svg = d3.select('svg')
	const element = document.querySelector('.graph-container')

	console.log(element)

	const margin = { top: 200, right: 10, bottom: 20, left: -100 }

	const width = 1000 - margin.right - margin.left
	const height = 1000 - margin.top - margin.bottom

	const xScale = d3.scaleLinear()
	    .domain([0, 20-1]) // input
		.range([0, width]); // output

	const yScale = d3.scaleLinear()
		.domain([0, 1]) // input 
		.range([height, 0]); // output 

	const dataset = d3.range(20).map(elem => ({"y": d3.randomUniform(1)() }))

	dataset.push({"y": d3.randomUniform(1)() })

	const x_axis = d3.axisLeft().scale(yScale)

	svg.append('g')
		.attr('transform', 'translate(0, 0)')
		.call(x_axis)

	// svg.append('g').call(xAxis)
	// svg.append('g').call(yAxis)

	// svg.selectAll('.dot')
	// .data(dataset).enter()	// for each point in the data-set
	// .append('circle')		// append a circle
	// .attr('cx', (d, i) => xScale(i))
	// .attr('cy', d => yScale(d.y))
	// .attr('r', 5)

	const line = d3.line()
		.x((data, index) => xScale(index))
		.y(point => yScale(point.y))
		.curve(d3.curveNatural)

	svg.append('path')
	.attr('width', width + margin.left + margin.right)
	.attr('height', height + margin.top + margin.bottom)
	.attr('d', line(dataset))
	.attr('stroke', 'red')
	.attr('fill', 'none')
	.append('g')
		.attr('transform', `translate(${margin.left}, ${margin.top})`)
```

(sorry it's not the prettiest, threw it together in an afternoon as a proof of concept)
