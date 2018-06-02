from datetime import date
from ledger_suite.parse.TDCSVParser import TDCSVParser
from ledger_suite.ledger.Amount import Amount
from ledger_suite.ledger.Transaction import Transaction

csvEntry = {
    'transactionDate': '12/30/2017',
    'transactionDescription': 'PAYROLL',
    'withdrawl': '',
    'deposit': '5000.00',
    'balance': '5137.96'
}

def test_parser():
    parser = TDCSVParser('Assets:TD Chequing')
    parsedTransaction = parser.parse(csvEntry)
    assert parsedTransaction == Transaction(
        date(2017, 12, 30),
        'PAYROLL',
        [
            Amount('Assets:TD Chequing', 5000.00),
            Amount(None, -5000.00, True)
        ]
    )
