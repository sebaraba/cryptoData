import plotly.graph_objects as go
import pandas as pd
import pymongo
import json
import bson

from datetime import datetime

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDatabase = mongoClient["cryptoData"]
mongoTable = mongoDatabase["bitcoinPrices"]
mongoEntries = mongoTable.find({}).limit(50)
mongoData = pd.DataFrame(list(mongoEntries))


def grouByTimestamp(element):
    return element['timestamp'][10:]


for i in mongoData['_id']:
    print(i)

# for i in list(mongoEntries):
#     print(i)
