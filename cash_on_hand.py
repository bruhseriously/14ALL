import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
coh_csv = Path.cwd()/'csv_reports'/'Cash on Hand.csv'

def cashonhand_function(forex):
    if coh_csv.exists():
        with coh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            day = []
            cash = []
            next(reader)
            for row in reader:
                day.append(float(row[0]))
                cash.append(float(row[1]) * forex)
    else:
        print('cashonhand_function: coh_csv does not exist')
    count = 0
    for amount in range(len(cash) - 1):
        diff = cash[amount] - cash[amount + 1]
        if diff > 0:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                    text = file.write(f'\n[CASH DEFICIT] DAY: {day[amount + 1]}, AMOUNT: SGD{diff:.2f}')
                    count += 1
            else:
                print('cashonhand_function: file_path does not exist')
    if count == 0:
        if file_path.exists():
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                text = file.write(f'\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        else:
            print('cashonhand_function: file_path does not exist')