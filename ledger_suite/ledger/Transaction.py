import datetime
from dateutil.parser import parse

class Transaction():
    def __init__(self, date, payee, amounts, cleared = True, notes = '', tags = {}):
        self.date = date
        self.payee = payee
        self.amounts = amounts
        self.cleared = cleared
        self.notes = notes
        self.tags = tags

    def __eq__(self, other):
        amounts = True
        for (a1, a2) in zip(self.amounts, other.amounts):
            amounts = amounts and (a1 == a2)
        return self.date == other.date and \
            self.payee == other.payee and \
            self.cleared == other.cleared and \
            self.notes == other.notes and \
            self.tags == other.tags and \
            amounts

    def __str__(self):
        dateString = parse(str(self.date)).strftime('%Y/%m/%d')
        clearedString = '*' if self.cleared == True else '!'
        amountsString = ''
        for amount in self.amounts:
           amountsString += str(amount)
           amountsString += '\n\t'
        return '%s %s %s\n\t%s' % (dateString, clearedString, self.payee, amountsString)

    def validTransaction(self):
        if len(self.amounts) < 2:
            return false
        sum = 0
        for amount in self.amounts:
            sum += amount.value
        return sum == 0
