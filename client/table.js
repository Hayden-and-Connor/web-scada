const Table = {}

Table.DomTemplates = {}

const DomTemplates = {}

// take an html string and return a dom element defined by that string
DomTemplates.render = function(html) {
	const template = document.createElement('template')
	template.innerHTML = html.trim()
	return template.content
}

Table.DomTemplates.row = function({label, value, unit}){
	const template = `
		<tr class="state__element row--${label}">
			<td class="state-element__label">${label}: </td>
			<td>
				<span class="state-element__value">${value}</span>
				<span class="state-element__unit">${unit}</span>
			</td>
		</tr>`

	return DomTemplates.render(template)
}

Table.append_row = function(label, data){
	const target = Utils.DomQuery('.state__list')[0]
	target.appendChild(Table.DomTemplates.row({label, ...data}))
}

Table.update_row = function(label, data){

	// get all the rows with this key in the table
	const current_rows = Utils.DomQuery(`.state__element.element--${label}`)

	console.log(current_rows)

	if(current_rows.length == 0) {
		Table.append_row(label, data)
	} else {
		const row = current_rows[0]

		row.querySelector('.state-element__label').innerHTML = `${label}: `
		row.querySelector('.state-element__value').innerHTML = `${data.value}`

	}
}

socket.on('data', function(data){
	console.log(data)

	for(const label in data) {
		const { value, unit } = data[label]

		console.log({label, value, unit})

		Table.update_row(label, {value, unit})

		// make new table row and append it to table
		// const row = Table.DomTemplates.row({label, value, unit})

		// const target = Utils.DomQuery('.state__list')[0]
	}
})