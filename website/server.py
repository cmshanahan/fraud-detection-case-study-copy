## Server Flask File

from flask import Flask, render_template, request, jsonify, Response
import pickle
import numpy as np
import pandas as pd

## Create the app object that will route our calls
app = Flask(__name__)


## Rendering the home page HTML
@app.route('/', methods = ['GET'])
def home():
	return render_template('home.html')

## Rendering the mpg prediction page html
@app.route('/mpg', methods = ['GET'])
def mpg():
	return render_template('mpg.html')

## Calculating and posting the linear regression model prediction
modelLR = pickle.load(open('linreg.p', 'rb'))
@app.route('/inferenceLR', methods = ['POST'])
def inferenceLR():
	req = request.get_json()
	print(req)

	## Getting params from request
	c,h,w = [req['cylinders'], req['horsepower'], req['weight']]
	prediction = list(modelLR.predict([[c,h,w]])) ## Getting prediction

	## Returning json formatted output (.js file grabs 'prediction')
	return jsonify({'c':c, 'h':h, 'w':w, 'prediction':np.round(prediction[0],3)})


modelRF = pickle.load(open('randomf.p', 'rb'))
@app.route('/inferenceRF', methods = ['POST'])
def inferenceRF():
	req = request.get_json()
	print(req)

	params = [req['cylinders'], 
			  req['displacement'],
		 	  req['horsepower'],
		 	  req['weight'],
		 	  req['acceleration'],
		 	  req['model'],
		 	  req['origin']]
	print(params)

	## Checking if all the parameters are entered
	if None in params:
		return jsonify({'prediction':'Need to enter all data'})

	## If all entered getting and posting prediciton
	else:
		prediction = list(modelRF.predict([params]))
		
		return jsonify({'c':params[0],
						'h':params[1],
						'w':params[2],
						'prediction':prediction[0]})


@app.route('/plot', methods = ['GET'])
def plot():
	df = pd.read_csv('cars.csv')
	data = list(zip(df.mpg, df.weight))
	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3333, debug=True)


