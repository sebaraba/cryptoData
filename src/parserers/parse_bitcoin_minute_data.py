import csv
from datetime import datetime
import json
import pymongo
from datetime import datetime

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDatabase = mongoClient["cryptoData"]
mongoTable = mongoDatabase["bitcoinPrices"]

def csvToMongodb(data):
    timestamp = str(datetime.fromtimestamp(int(data[0][:-3])))
    return {
        "_id": "BTC:" + timestamp,
        "symbol": "BTC",
        "convert": "USD",
        "open": data[1],
        "close": data[2],
        "high": data[3],
        "low": data[4],
        "tradedVolume": data[5],
        "timestamp": timestamp
    }

with open('../data/btcusd.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    mongoData = map(csvToMongodb, csv_reader)
    mongoTable.insert_many(mongoData, ordered=False)
