 #This example uses python -m pip install requests

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2ab3a716-103b-4de5-860e-b87e0ec15bce',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  f = open("07_April_AllCoins.txt", "w+")
  f.write(response.text)
  f.close()
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)