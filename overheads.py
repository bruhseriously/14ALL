import csv
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
oh_csv = Path.cwd()/'csv_reports'/'Overheads.csv'

def overheads_function(forex):
    if oh_csv.exists():
        with oh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            oh = {}
            next(reader)
            for row in reader:
                oh[row[0]] = float(row[1]) * forex
    else:
        print('overheads_functionn: File path does not exist')    
    highest_value = 0
    for key in oh:
        if oh[key] > highest_value:
            highest_value = oh[key]
    for key, value in oh.items():
        if value == highest_value:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                    text = file.write(f'\n[HIGHEST OVERHEADS] {key.upper()}: SGD{value:.2f}')
