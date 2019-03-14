from pymongo import MongoClient
import pickle
import numpy as np
import pandas as pd


client = MongoClient()

db = client['fraud_database']	# Access/Initiate Database
tab = db['data_table']			# Access/Initiate Table


## Read in the pickle model
model = pickle.load(open('model_name', 'rb'))

## Command to get 50 most recent entrys into DB
tab.postings.find().sort({_id:1}).limit(50);


tab.update_one({'name':'noah'}, {'$set':{'toes':9}})