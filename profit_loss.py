import csv
from pathlib import Path

# set file path to summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
# set file path to profit and loss csv
pl_csv = Path.cwd()/'csv_reports'/'Profit and Loss.csv'

# create function to find profit defict or surplus
def profitloss_function(forex):
    if pl_csv.exists():
        with pl_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            # create a reader object
            reader = csv.reader(csvfile)
            # create empty list for days
            day = []
            # create empty list for net profit each day
            netprofit = []
            # skip headers in csv file
            next(reader)
            # for each row in csv file
            for row in reader:
                # append days in csv file to empty list days
                day.append(float(row[0]))
                # append net profit each day to empty list netprofit
                netprofit.append(float(row[4]) * forex)
    else:
        print('profitloss_function: pl_csv does not exist')
    # set global counter
    count = 0
    # for each net profit amount except for the last
    for amount in range(len(netprofit) - 1):
        # find difference in net profit between each day
        diff = netprofit[amount] - netprofit[amount + 1]
        # if the next day's amount is higher, the difference will be positive
        if diff > 0:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                    # write profit defict with corresponding day and difference amount rounded off to 2d.p. in summary_report.txt
                    text = file.write(f'\n[PROFIT DEFICIT] DAY: {day[amount + 1]}, AMOUNT: SGD{diff:.2f}')
                    # prevents profit surplus line from being written
                    count += 1
            else:
                print('profitloss_function: file_path does not exist')
    # count variable only lets profit surplus be written if there is no profit defict
    if count == 0:
        if file_path.exists():
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                # write profit surplus in summary_report.txt
                text = file.write(f'\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        else:
            print('profitloss_function: file_path does not exist')
                