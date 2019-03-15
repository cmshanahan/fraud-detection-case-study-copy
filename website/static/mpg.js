
$(document).ready(function(){
	console.log('Document is ready')

	// Button config for Linear Regression Prediction
	$("#inferenceLR").click(async function(){
		console.log('button was clicked')

		const cylinders = parseFloat($('#cylinders').val());
		const horsepower = parseFloat($('#horsepower').val());
		const weight = parseFloat($('#weight').val());


		const data = {
			cylinders,
			horsepower,
			weight
		}

		console.log(data)

		const response = await $.ajax('/inferenceLR', {
			data: JSON.stringify(data),
			method: "post",
			contentType:'application/json'
		})

		console.log(response)
		$('#mpgLR').val(response.prediction)

	})

	// Button config for Random Forrest Prediction
	$("#inferenceRF").click(async function(){
		console.log('button was clicked')

		const cylinders = parseFloat($('#cylinders').val());
		const horsepower = parseFloat($('#horsepower').val());
		const weight = parseFloat($('#weight').val());
		const origin = parseFloat($('#origin').val());
		const displacement = parseFloat($('#displacement').val());
		const acceleration = parseFloat($('#acceleration').val());
		const model = parseFloat($('#model').val());


		const data = {
			cylinders,
			horsepower,
			weight,
			origin,
			displacement,
			acceleration,
			model
		}

		console.log(data)

		const response = await $.ajax('/inferenceRF', {
			data: JSON.stringify(data),
			method: "post",
			contentType:'application/json'
		})

		console.log(response)
		$('#mpgRF').val(response.prediction)

	})

	// Scatter button
	$("#scatter-button").click(async function(){
		console.log('scatter button was clicked')

		const response = await $.ajax('/plot')

		console.log(response)

		const mpg = response.map(a=>a[0])
		const weight = response.map(a=>a[1])
		console.log(mpg)

		const trace = [{
			x:weight,
			y:mpg,
			mode:'markers',
			type:'scatter'
		}];

		const layout = {
			xaxis:{
				title:'weight'
			},
			yaxis:{
				title:'mpg'
			},
			title:'Scatter of MPG vs Weight',
			width:700,
			height:300
		}
		Plotly.plot($('#graph1')[0], trace, layout)
		$('#scatter-button').hide()

	})

})








