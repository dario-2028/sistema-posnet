class CreditCard:
    def __init__(self, bankEntity, cardNumber, balance, holder):
        self.bankEntity = bankEntity
        self.cardNumber = cardNumber
        self.balance = balance
        self.holder = holder

    def getBankEntity(self):
        return self.bankEntity

    def setBankEntity(self, bankEntity):
        self.bankEntity = bankEntity

    def getCardNumber(self):
        return self.cardNumber

    def setCardNumber(self, cardNumber):
        self.cardNumber = cardNumber

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getHolder(self):
        return self.holder

    def setHolder(self, holder):
        self.holder = holder

    def __str__(self):
        return f"CreditCard [Bank Entity: {self.bankEntity}, Card Number: {self.cardNumber}, Balance: {self.balance}, Holder: {self.holder}]"

