import collections

from datetime import datetime
from parse.DataParser import DataParser
from ledger.Transaction import Transaction
from ledger.Amount import Amount

class TDCSVParser(DataParser):
    def __init__(self, accountName):
        self.accountName = accountName

    def parse(self, entry):
       [month, day, year] = entry['transactionDate'].split('/')
       transactionDate = datetime(int(year), int(month), int(day))
       cleared = transactionDate <= datetime.today()
       payee = entry['transactionDescription']
       amounts = []
       try:
           withdrawl = float(entry['withdrawl'])
           amounts += [Amount(None, withdrawl), Amount(self.accountName, -withdrawl, True)]
       except ValueError:
           pass
       try:
           deposit = float(entry['deposit'])
           amounts += [Amount(self.accountName, deposit), Amount(None, -deposit, True)]
       except ValueError:
           pass
       return Transaction(transactionDate, payee, amounts, cleared)

    def parseAll(self, data):
        transactions = []
        for entry in data:
            transactions += [self.parse(entry)]
        return transactions

    def fields(self):
        return [
            'transactionDate',
            'transactionDescription',
            'withdrawl',
            'deposit',
            'balance'
        ]
