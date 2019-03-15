import pickle
import clean
import pandas as pd

from pymongo import MongoClient

## Convert dictionary into pandas frame
def make_pandas(entry):
	df = pd.DataFrame(entry)

	## Clean the data
	return clean.clean_data(df)

## Predict on the new entry
def predict(model, cleaned):

	## Selecting on important columns and getting preds
	X = cleaned[cols].values
	preds = model.predict_proba(X_test)[:,1]

	return preds



if __name__ == '__main__':

	## Read in the pickle model
	model = pickle.load(open('models/rf_model.p', 'rb'))

	## Connect to the Mongo DB
	client = MongoClient('localhost', 27017)
	db = client['fraud']		## Mongo database name
	table = db['events_new2']	## Mongo table name

	## Read in the first X new entries
	r = table_new.find().sort([('_id', -1)]).limit(1)

	## Transforming data
	cleaned = make_pandas(r[0])

	## Predict on the new data
	prediction = predict(model, cleaned)
	

