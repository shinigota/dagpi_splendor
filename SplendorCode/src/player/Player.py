import Tools
import Game

class Player:

    def __init__(self):
        self.purchasedCards = []
        self.reservedCards = []
        self.ownedTiles = []
        self.bank = []
        self.position = None
        self.nickname = None

        for type in Game.GameBoard.getTypes():
            self.bank.append(self.initBank(type))

    def initBank(self, type):
        tkStack = Tools.TokenStack()
        tkStack.setType(type)
        tkStack.setNbToken(0)
        return tkStack

    def addPurchasedCard(self, card):
        self.purchasedCards.append(card)

    def delPurchasedCard(self, card):
        self.purchasedCards.remove(card)
        del card



    def addReservedCard(self, card):
        self.reservedCards.append(card)

    def delReservedCard(self, card):
        self.reservedCards.remove(card)
        del card



    def addOwnedTile(self, tile):
        self.ownedTiles.append(tile)

    def delOwnedTile(self, tile):
        self.ownedTiles.remove(tile)
        del tile
