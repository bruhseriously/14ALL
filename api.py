import requests
from pathlib import Path

api_key = 'F2UE00AWKLCI7DKV'
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
response = requests.get(url)
data = response.json()

file_path = Path.cwd()/'summary_report.txt'

def api_function():
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    if file_path.exists():
        with file_path.open(mode = 'w', encoding = 'UTF-8', errors = 'ignore') as file:
            text = file.write(f'[REAL TIME CURRENCY COVERSION RATE] USD1 = SGD{forex:.5f}')
    else:
        print('api_function: file_path does not exist')
    return forex