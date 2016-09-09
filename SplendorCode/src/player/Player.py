from src.element.TokenStack import TokenStack
from src.game.GameBoard import GameBoard
from src.element.Tile import Tile
from src.element.Card import Card


class Player:
    nickname = None
    position = None
    reserved_cards = None
    purchased_cards = None
    owned_tiles = None
    bank = None

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

    def add_purchased_card(self, card):
        self.purchased_cards.append(card)

    def del_purchased_card(self, card):
        self.purchased_cards.remove(card)
        del card

    def add_reserved_card(self, card):
        self.reserved_cards.append(card)

    def del_reserved_card(self, card):
        self.reserved_cards.remove(card)
        del card

    def add_owned_tile(self, tile):
        self.owned_tiles.append(tile)

    def del_owned_tile(self, tile):
        self.owned_tiles.remove(tile)
        del tile


    def addDifferentTokens(self, types):
        for type in types:
            for tkStack   in self.bank:
                if tkStack.type == type:
                    tkStack.addToken(1)

    def addSameToken(self, type):
        for tkStack in self.bank:
            if tkStack.type == type:
                tkStack.addToken(2)


