import csv
from pathlib import Path

# create file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
# create file path to overheads.csv
oh_csv = Path.cwd()/'csv_reports'/'Overheads.csv'

# create function to find highest overheads and value
def overheads_function(forex):
    '''
    - This function accepts one parameter, forex
    - The function will find the highest overhead category and its value converted 
      to SGD using the real time exchange rate from the API call. 
    '''
    if oh_csv.exists():
        with oh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            # create a reader object
            reader = csv.reader(csvfile)
            # empty dictionary oh to store overheads and respective amounts
            oh = {}
            # skip headers in csv file
            next(reader)
            # for each row in the csv file
            for row in reader:
                # appends overhead category as key and respective amount converted to sgd as value to oh
                oh[row[0]] = float(row[1]) * forex
    else:
        print('overheads_function: oh_csv does not exist')    
    # set global variable
    highest_value = 0
    # for each overhead in dictionary oh
    for key in oh:
        # makes the highest value replace the global variable
        if oh[key] > highest_value:
            highest_value = oh[key]
    # for overheads and respective values in dictionary oh
    for key, value in oh.items():
        # if the key's value is the highest value
        if value == highest_value:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                    # write highest overheads category and amount rounded off to 2d.p.
                    text = file.write(f'\n[HIGHEST OVERHEADS] {key.upper()}: SGD{value:.2f}')
            else:
                print('overheads_function: file_path does not exist')