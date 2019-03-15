import pickle
import models.clean as clean
import pandas as pd

from pymongo import MongoClient

## Convert dictionary into pandas frame
def make_pandas(entry):

	prev = entry['previous_payouts']
	del entry['previous_payouts']

	df = pd.DataFrame.from_dict(entry)

	## Clean the data
	return clean.clean_data_new(df)

## Predict on the new entry
def predict(model, cleaned, cols):

	## Selecting on important columns and getting preds
	X = cleaned[cols].values
	preds = model.predict_proba(X)[:,1]

	return preds



def get_prediction(d):

	## Read in the pickle model
	model = pickle.load(open('website/models/rf_model.p', 'rb'))

	# ## Read in the first X new entries
	# r = table.find().sort([('_id', -1)]).limit(2)

	## Transforming data
	cleaned = make_pandas(d)
	

	## Predict on the new data
	rf_cols = ['USD','GBP','CAD','AUD','EUR','NZD','MXN', 
		   'age_dummy',
		   'user_age',
		   'payoutdiff',
		   'gts',
		   'num_order',
		   'num_payouts',
		   'payee_exists']
	return predict(model, cleaned, rf_cols)
	

