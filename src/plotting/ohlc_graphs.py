import plotly.graph_objects as go
import pandas as pd
import pymongo
import json
import bson

from datetime import datetime

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDatabase = mongoClient["cryptoData"]
mongoTable = mongoDatabase["bitcoinPrices"]
mongoEntries = mongoTable.find({}).limit(100)
mongoData = pd.DataFrame(list(mongoEntries))


# hovertext=[]
# for entry in mongoEntries:
#     hovertext.append('Open: '+str(entry['open'])+'<br>Close: '+str(entry['close']))

# fig = go.Figure(data=go.Ohlc(x=mongoData['timestamp'],
#                 open=mongoData['open'],
#                 high=mongoData['high'],
#                 low=mongoData['low'],
#                 close=mongoData['close'],
#                 text=hovertext,
#                 hoverinfo='text'))

# fig.update_layout(
#     title='Bitcoin Minute Prices',
#     yaxis_title='Bitcoin Price',
#     annotations=[dict(
#         x='2013-04-01', y=0.05, xref='x', yref='paper',
#         showarrow=False, xanchor='left', text='Increase Period Begins')]

# )

# fig.show()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']))

fig.update_layout(
    title='The Great Recession',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)

fig.show()