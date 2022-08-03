import requests
from pathlib import Path

# assign api key to api_key
api_key = 'F2UE00AWKLCI7DKV'
# assign api url to url
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
# request access to data using .get and assign it to response
response = requests.get(url)
# retrieve data with .json from response and save it as data
data = response.json()

# set file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'

# create function to extract conversion rate for usd to sgd from alphavantage
def api_function():
    '''
    - This function extracts the real time currency exchange rate for USD to SGD from AlphaVantage.
    - The exchange rate will then be written in summary_report.txt.
    '''
    # index exchange rate in data and convert to float before assigning to forex
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    if file_path.exists():
        with file_path.open(mode = 'w', encoding = 'UTF-8', errors = 'ignore') as file:
            # write exchange rate in summary_report.txt 
            text = file.write(f'[REAL TIME CURRENCY COVERSION RATE] USD1 = SGD{forex:.5f}')
    else:
        print('api_function: file_path does not exist')
    return forex