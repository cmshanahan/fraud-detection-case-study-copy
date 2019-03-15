from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['fraud']
table = db['events_new2']

import requests
api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
#broken link
#url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
url = 'http://galvanize-case-study-on-fraud.herokuapp.com/data_point'
sequence_number = 0
#response = requests.get(url, json={'api_key': api_key,
#                                'sequence_number': sequence_number})
response = requests.get(url)
raw_data = response.json()



import time
check = True
while check:
    try:
        response = requests.get(url)
        raw_data = response.json()
        table.insert_one(raw_data)
        sequence_number += 1
        print(sequence_number)
    except:
        print('duplicate')
        
    time.sleep(180)
