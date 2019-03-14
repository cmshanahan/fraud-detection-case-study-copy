import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## To upsumple no fraud class
#from imblearn.over_sampling import SMOTE


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, make_scorer


def cross_val_mse_r2(X_train, y_train, func):

	rec = sum(cross_val_score(func, X_train, y_train, scoring='recall'))/3
	auc = sum(cross_val_score(func, X_train, y_train, scoring='roc_auc'))/3

	func_name = str(func.__class__.__name__)

	print("{0:27} Train CV | Recall: {1:5.4} | AUC: {2:5.4}".format(func_name, rec, auc))
	return rec, auc


def get_confusion(preds, target):
	TP = (preds & target).sum()
	FP = ((preds - target) == 1).sum()
	TN = ((preds + target) == 0).sum()
	FN = ((preds - target) == -1).sum()

	confusion = [TP, FP,
				 FN, TN]

	actual_p = target.sum()
	actual_n = len(target) - actual_p

	scoring = [TP/actual_p, FP/actual_n,
			   FN/actual_p, TN/actual_n ]


	cons = ['TP', 'FP', 'FN', 'FP']
	scos = ['TPR', 'FPR', 'FNR', 'TNR']
	for i in range(4):
		print("{0:2}: {1:5}   |   {2:3}: {3:5.3}".format(cons[i],confusion[i],scos[i],scoring[i]))

	return (confusion, scoring)


def clean_data(df):

	## Age Dummy if over specified number
	df['age_dummy'] = df['user_age'].apply(lambda x: 1 if x > 0 else 0)

	## Adding Event Diff Col
	df['eventdiff'] = df['event_published'] - df['event_end']

	## Adding Payout date diff col 
	df['payoutdiff'] = df['approx_payout_date'] - df['event_created']

	return df


## Cleaning the target data into 1 and 0
def get_target(df):

	## Signals fraud account 
	fraud_accts = set(['fraudster_event', 'fraudster', 'fraudster_att'])

	new_df = df.copy()
	new_df['fraud'] = df['acct_type'].apply(lambda x: 1 if x in fraud_accts else 0)
	new_df.drop('acct_type', axis=1, inplace=True)	## Dropping old col
	return new_df['fraud'].values


def get_features(df):
	return df[['user_age', 'age_dummy']].values
	


if __name__ == '__main__':
	df = pd.read_json('data/data.json')

	## Clean the data
	cleaned = clean_data(df)

	## Getting targets and cleaned features
	y = get_target(cleaned)
	X = get_features(cleaned)

	# Resampling the data to avoid non fraud bias
	#method = SMOTE(kind='regular')
	#X_resampled, y_resampled = method.fit_sample(X, y)


	X_train, X_test, y_train, y_test = train_test_split(X,
														y,
														test_size=.2,
														random_state=1)

	model = LogisticRegression()
	model.fit(X_train, y_train)
	preds = model.predict_proba(X_test)[:,1]

	preds = (preds > .2).astype(int)

	(conf, score) = get_confusion(preds, y_test)

	cross_val_mse_r2(X_train, y_train, model)



