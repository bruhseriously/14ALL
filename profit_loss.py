import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
pl_csv = Path.cwd()/'csv_reports'/'Profit and Loss.csv'

def profitloss_function(forex):
    if pl_csv.exists():
        with pl_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile: