from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import urllib.request
import json
import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cryptoMetrics"]
mycol = mydb["priceMarketCapMetrics"]

priceDataURL = "https://api.nomics.com/v1/exchange-rates/history?key=42c185144866ea1fee1d9a2b994bbc35&currency=BTC&start=2010-01-01T00%3A00%3A00Z&end=2020-04-01T00%3A00%3A00Z"
marketCapDataURL = "https://api.nomics.com/v1/market-cap/history?key=42c185144866ea1fee1d9a2b994bbc35&start=2010-01-01T00%3A00%3A00Z&end=2020-04-01T00%3A00%3A00Z"
totalMarketCapURL = "https://api.nomics.com/v1/volume/history?key=42c185144866ea1fee1d9a2b994bbc35&start=2018-04-14T00%3A00%3A00Z&end=2018-05-14T00%3A00%3A00Z&convert=USD"

def bringTogether(x, y, z):
    mycol.insert_one({"_id":"Btc-"+x, "name": "Bitcoin", "price": y, "marketCap": z, "timestamp": x})
    
try:
  marketCapData = urllib.request.urlopen(marketCapDataURL).read()
  priceData = urllib.request.urlopen(priceDataURL).read()
  parsedMarketCap = json.loads(marketCapData)
  parsedPriceData = json.loads(priceData)
  
  prices = map(lambda x: x['rate'], parsedPriceData)
  marketCap = map(lambda x: x['market_cap'], parsedMarketCap)
  timestamps = map(lambda x: x['timestamp'], parsedMarketCap)

  toWrite = map(bringTogether, timestamps, prices, marketCap)

  for key in toWrite:
      print(key)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)