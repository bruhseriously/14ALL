import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
oh_csv = Path.cwd()/'csv_reports'/'Overheads.csv'

def overhead_function(forex):
    if oh_csv.exists():
        with oh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile: