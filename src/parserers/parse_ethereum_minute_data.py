import csv
from datetime import datetime
import json
import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cryptoPlots"]
mycol = mydb["minutePrices"]

def csvToMongodb(data):
    timestamp = str(datetime.fromtimestamp(int(data[0][:-3])))
    return {
        "_id": "ETH:" + timestamp,
        "symbol": "ETH",
        "convert": "USD",
        "open": data[1],
        "close": data[2],
        "high": data[3],
        "low": data[4],
        "tradedVolume": data[5],
        "timestamp": timestamp
    }

with open('../data/ethusd.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    mongoData = map(csvToMongodb, csv_reader)

    # mycol.insert_many(mongoData, ordered=False)
    