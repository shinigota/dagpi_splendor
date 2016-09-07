class Card:

    def __init__(self):
        self.points = None
        self.incomeGem = None
        self.purchaseGems =[]


    def setIncomeGem(self, tokenStack):
        self.incomeGem = tokenStack


    def addPurchaseGems(self, tokenStack):
        self.purchaseGems.append(tokenStack)

    def delPurchaseGems(self, tokenStack):
        self.purchaseGems.remove(tokenStack)
        del tokenStack
