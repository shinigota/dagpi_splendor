from src.element.TokenStack import TokenStack
from src.game.GameBoard import GameBoard
from src.element.Tile import Tile
from src.element.Card import Card

class Player:

    def __init__(self, nickname, position):
        self.purchasedCards = [Card]
        self.reservedCards = [Card]
        self.ownedTiles = [Tile]
        self.bank = [TokenStack]
        self.position = position
        self.nickname = nickname

        for type in GameBoard.types:
            self.bank.append(self.initBank(type))

    def initBank(self, type):
        tkStack = TokenStack()
        tkStack.type = type
        tkStack.nbToken = 0
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

    def addDifferentTokens(self, types):
        for type in types:
            for tkStack   in self.bank:
                if tkStack.type == type:
                    tkStack.addToken(tkStack, 1)

    def addSameToken(self, type, nbToken):
        for tkStack in self.bank:
            if tkStack.type == type:
                tkStack.addToken(tkStack, nbToken)

