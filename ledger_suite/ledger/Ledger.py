import re
from datetime import datetime
from ledger.Transaction import Transaction
from ledger.Amount import Amount

class Ledger():
    def __init__(self, entries=[]):
        self.entries = entries

    def parse(file):
        f = open(file, 'r')
        line = f.readline()
        transactionRegex = re.compile(r'^(\d{4}/\d{2}/\d{2})\s*(\*?)\s*(.*)')
        amountRegex = re.compile(r'^[ \t]\s*((\w+\:?)+)\s*(.*)$')

        # If we parse a date at the beginning of the line its a new transaction
        newTransaction = re.compile(r'^\d{4}/\d{2}/\d{2}')
        # if we parse a tab its a continuation of the transaction
        continuedTransaction = re.compile(r'^[ \t]')
        # if we parse a blank line its the end of the transaction
        endTransaction = re.compile(r'^$')
        transactions = []
        while line:
            if newTransaction.search(line):
                date = re.search(transactionRegex, line).group(1)
                [year, month, day] = date.split('/')
                transactionDate = datetime(int(year), int(month), int(day))
                cleared = re.search(transactionRegex, line).group(2)
                payee = re.search(transactionRegex, line).group(3)
                amounts = []
                tags = []
                line = f.readline()
                while continuedTransaction.search(line):
                    # Either an amount line
                    if amountRegex.search(line):
                        account = re.search(amountRegex, line).group(1)
                        value = re.search(amountRegex, line).group(3)
                        amounts += [Amount(account, value)]
                    # or a tag line
                    else:
                        tag = {}
                    line = f.readline()
                transactions += [Transaction(transactionDate, payee, amounts)]
            else:
                line = f.readline()

        return Ledger(transactions)
