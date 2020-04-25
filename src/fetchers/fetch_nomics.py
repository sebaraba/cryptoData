import urllib
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import urllib.request
import json


url = "https://api.nomics.com/v1/exchange-rates/history?key=demo-26240835858194712a4f8cc0dc635c7a&currency=BTC&start=2018-04-01T00%3A00%3A00Z&end=2018-04-02T00%3A00%3A00Z"

parsed = json.loads(urllib.request.urlopen(url).read())
print(json.dumps(parsed, indent=4, sort_keys=True))