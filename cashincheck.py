#!/usr/bin/python3
from pprint import pprint #нахне нужен, удобно чекать джисон
import requests
import json
url = 'https://edge.qiwi.com/payment-history/v2/persons/79688569979/payments?rows=10'
headers = {
	'Accept' : 'application/json',
	'Content-Type' : 'application/json',
	'Authorization' : 'Bearer you_token'
}
r = requests.get(url, headers = headers)
r.raise_for_status() # do not create the result file until json is parsed
data = r.json()
pprint(data)  
with open('cash.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

