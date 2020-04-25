import pymongo
import db.HistoryEntity
from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["coinMarketCap"]
mycol = mydb["coinMetrics"]

coinMetrics = open("03_June_AllCoins.txt", "r+")
coinMetrics


h = {
    "name": "Ethereum",
    "usdPrice": 100,
    "marketCap": 100000,
    "totalSupply": 10342,
    "date": "10/02/2019"
}

x = mycol.insert_one(h)