# import things
from flask_table import Table, Col
from pymongo import MongoClient


# Declare your table
class ItemTable(Table):
    event = Col('Event ID')
    fraud_class = Col('Fraud Classification')
    fraud_prob = Col('Probability of Fraud')

# Get some objects
class Item(object):
    def __init__(self, event, fraud_class, fraud_prob):
        self.event = event
        self.fraud_class = fraud_class
        self.fraud_prob = fraud_prob


client = MongoClient('localhost', 27017)
db = client['fraud']
table = db['events']

r = table.find().sort([('_id', -1)]).limit(50)

items = []
for entry in r:
    items.append(Item(entry['Object_id'], entry['Class'], entry['Prediction']))


# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template