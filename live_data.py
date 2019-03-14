import requests
api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'
url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
sequence_number = 0
response = requests.post(url, json={'api_key': api_key,
                                    'sequence_number': sequence_number})
raw_data = response.json()
