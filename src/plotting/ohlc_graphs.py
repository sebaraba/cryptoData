import plotly.graph_objects as go
import pandas as pd
import pymongo
import json
import bson

from datetime import datetime

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDatabase = mongoClient["cryptoData"]
mongoTable = mongoDatabase["bitcoinPrices"]
mongoEntries = mongoTable.find({}).limit(1)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')


hovertext=[]
for entry in mongoEntries:
    hovertext.append('Open: '+str(entry['open'])+'<br>Close: '+str(entry['close']))

print(mongoEntries['timestamp'])


fig = go.Figure(data=go.Ohlc(x=mongoEntries['timestamp'][:10],
                open=mongoEntries['open'],
                high=mongoEntries['high'],
                low=mongoEntries['low'],
                close=mongoEntries['close'],
                text=hovertext,
                hoverinfo='text'))
fig.show()