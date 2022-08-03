import requests
from pathlib import Path

api_key = 'F2UE00AWKLCI7DKV'
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
response = requests.get(url)
data = response.json()

file_path = Path.cwd()/'summary_report.txt'

def api_function():