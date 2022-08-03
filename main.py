import api, cash_on_hand, overheads, profit_loss
from pathlib import Path

# set file path to create summary_report.txt
file_path = Path.cwd()/'summary_report.txt'
file_path.touch()

# create function to run all other functions
def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.cashonhand_function(forex)
    profit_loss.profitloss_function(forex)

main()