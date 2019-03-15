import pandas as pd
import numpy as np


######################################################
################## CLEANING ##########################

def clean_data(df):

	## Age Dummy if over specified number
	df['age_dummy'] = df['user_age'].apply(lambda x: 1 if x > 0 else 0)

	## Adding Payoutdate and Eventdate Diff columns
	df['eventdiff'] = df['event_published'] - df['event_end']
	df['payoutdiff'] = df['approx_payout_date'] - df['event_created']

	## Getting dummies on curreny and delivery method
	df = pd.concat([df, pd.get_dummies(df.currency)], axis=1);
	df = pd.concat([df, pd.get_dummies(df.delivery_method)], axis=1); 

	## Stripping the 
	df['payee_exists'] = [x.strip()=="" for x in df['payee_name']]

	return df

## Cleaning the target data into 1 and 0
def get_target(df):

	## Signals fraud account 
	fraud_accts = set(['fraudster_event', 'fraudster', 'fraudster_att'])

	new_df = df.copy()
	new_df['fraud'] = df['acct_type'].apply(lambda x: 1 if x in fraud_accts else 0)
	new_df.drop('acct_type', axis=1, inplace=True)	## Dropping old col
	return new_df['fraud'].values