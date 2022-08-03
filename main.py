import api, cash_on_hand, overheads, profit_loss
from pathlib import Path

# set file path to create summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
file_path.touch()

# create function to run all other functions
def main():
    '''
    - This function executes all the modules at once, in order of api_function, 
      overheads_function, cashonhand_function, profitloss_function.
    '''
    # assign forex from api_function to variable forex to be used in subsequent functions
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.cashonhand_function(forex)
    profit_loss.profitloss_function(forex)

main()