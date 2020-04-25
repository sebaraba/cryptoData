import re
import requests
from bs4 import BeautifulSoup

# Collect the coinmarketcap page
page = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190301&end=20200404')
f = open("resources/htmlPage.txt", "w+")
f.write(str(page))

f = open("resources/htmlPage.txt", "r+")
soup = BeautifulSoup(f.read(), 'html.parser')

# Parse dates
dates = soup.findAll(class_="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left")
for el in dates:
    m = re.match(r"(.*)class=\"\">(.*)</div></td>", str(el))


# Parse coin name
name = soup.find(class_="cmc-static-icon cmc-static-icon-1")
print(name)

