from src.element.GemStack import GemStack


class Card:

    def __init__(self, pts, ):
        self.points = pts
        self.incomeGem = None
        self.purchaseGems =[GemStack]

    def addPurchaseGems(self, gem):
        self.purchaseGems.append(gem)

    def delPurchaseGems(self, gem):
        self.purchaseGems.remove(gem)
        del gem
