import csv
from pathlib import Path

# set file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
# set file path to cash on hand.csv
coh_csv = Path.cwd()/'csv_reports'/'Cash on Hand.csv'

# create function to find cash deficit or surplus
def cashonhand_function(forex):
    '''
    - This function accepts one parameter, forex.
    - The function will calculate the difference in the cash on hand between each day and 
      convert it to SGD using the real time exchange rate from the API call.
    - If the cash on hand is not consecutively higher each day, the function will highlight 
      the day where cash on hand is lower than the previous day and the value difference
      in summary_report.txt.
    '''
    if coh_csv.exists():
        with coh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            # create a reader object
            reader = csv.reader(csvfile)
            # create empty list for days
            day = []
            # create empty list for amount of cash each day
            cash = []
            # skip headers in csv file
            next(reader)
            # for each row in the csv file
            for row in reader:
                # append days in csv file to empty list day
                day.append(float(row[0]))
                # append amount of cash each day converted to sgd to empty list cash
                cash.append(float(row[1]) * forex)
    else:
        print('cashonhand_function: coh_csv does not exist')
    # set a global counter
    count = 0
    # for each amount except the last
    for amount in range(len(cash) - 1):
        # calculate difference in cash on hand amount between each day
        diff = cash[amount] - cash[amount + 1]
        # if the next day's amount is higher, the difference will be positive
        if diff > 0:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                    # write cash deficit with corresponding day and difference amount rounded off to 2d.p. in summary_report.txt
                    text = file.write(f'\n[CASH DEFICIT] DAY: {day[amount + 1]}, AMOUNT: SGD{diff:.2f}')
                    # prevents cash surplus line from being written
                    count += 1
            else:
                print('cashonhand_function: file_path does not exist')
    # count variable only lets cash surplus be written if there is no cash deficit
    if count == 0:
        if file_path.exists():
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                # write cash surplus in summary_report.txt
                text = file.write(f'\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        else:
            print('cashonhand_function: file_path does not exist')