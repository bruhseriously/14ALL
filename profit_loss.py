import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
pl_csv = Path.cwd()/'csv_reports'/'Profit and Loss.csv'

def profitloss_function(forex):
    if pl_csv.exists():
        with pl_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            day = []
            netprofit = []
            next(reader)
            for row in reader:
                day.append(float(row[0]))
                netprofit.append(float(row[4]) * forex)
    else:
        print('profitloss_function: pl_csv does not exist')