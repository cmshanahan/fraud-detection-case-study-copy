## Server Flask File

from flask import Flask, render_template, request, jsonify, Response
import pickle
import numpy as np
import pandas as pd

import models.predict as predict

## Create the app object that will route our calls
app = Flask(__name__)


## Rendering the home page HTML
@app.route('/', methods = ['GET'])
def home():
	return render_template('home.html')


## Calculating and posting the linear regression model prediction
modelLR = pickle.load(open('models/rf_model.p', 'rb'))
@app.route('/prediction', methods = ['POST'])
def prediction():
	print("GET HERE")
	#req = request.get_json()
	#print(req)
	print("HEREEE")

	pred = predict.get_prediction()

	## Returning json formatted output (.js file grabs 'prediction')
	return jsonify({'prediction':np.round(prediction,3)})



# @app.route('/plot', methods = ['GET'])
# def plot():
# 	df = pd.read_csv('cars.csv')
# 	data = list(zip(df.mpg, df.weight))
# 	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3333, debug=True)


