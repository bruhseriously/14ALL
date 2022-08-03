import api, cash_on_hand, overheads, profit_loss
from pathlib import Path

file_path = Path.cwd()/'summary_report.txt'
file_path.touch()

def main():
    forex = api.api_function()
    overheads.overhead_function(forex)
    cash_on_hand.cashonhand_function(forex)
    profit_loss.profitloss_function(forex)

main()