const Table = {}

Table.DomTemplates = {}

const DomTemplates = {}

// take an html string and return a dom element defined by that string
DomTemplates.render = function(html) {
	const template = document.createElement('template')
	template.innerHTML = html.trim()
	return template.content
}

Table.DomTemplates.row = function({label, value}){
	const template = `
		<tr class="state__element row--${label}">
			<td class="state-element__label">${label}: </td>
			<td class="state-element__value">${value} </td>
		</tr>`

	return DomTemplates.render(template)
}

Table.append_row = function(label, value){
	const target = Utils.DomQuery('.state__list')[0]
	target.appendChild(Table.DomTemplates.row({label, value}))
}

Table.update_row = function(label, value){

	// get all the rows with this key in the table
	const current_rows = Utils.DomQuery(`.state__element.row--${label}`)

	if(current_rows.length == 0) {
		Table.append_row(label, value)
	} else {
		const row = current_rows[0]

		row.querySelector('.state-element__label').innerHTML = `${label}: `
		row.querySelector('.state-element__value').innerHTML = `${value}`
	}
}

Table.update_log = function(log){
	const target = Utils.DomQuery('.log__main')

	const new_log = DomTemplates.render(`
		<p>${log}</p>
	`.trim())

	target.appendChild(new_log)
}

socket.on('data', function(data){
	console.log(data)

	for(const label in data) {
		const { value, unit } = data[label]

		console.log({label, value})

		Table.update_row(label, value)

		Table.update_log(`new data: ${label}: ${value}`)

		// make new table row and append it to table
		// const row = Table.DomTemplates.row({label, value, unit})

		// const target = Utils.DomQuery('.state__list')[0]
	}
})