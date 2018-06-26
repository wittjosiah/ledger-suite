class Amount():
    def __init__(self, account = None, value = None, elideValue = False):
        self.account = account
        self.value = value
        self.elideValue = elideValue

    def __eq__(self, other):
        return self.account == other.account and \
            self.value == other.value and \
            self.elideValue == other.elideValue

    # TODO: make tabbing align for pretty ledgers
    def __str__(self):
        if self.elideValue:
            return str(self.account)
        else:
            return str(self.account) + '\t' + str(self.value)

    def validAmount(self):
        return self.account != None
