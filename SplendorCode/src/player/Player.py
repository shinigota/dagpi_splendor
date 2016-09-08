from src.element.TokenStack import TokenStack
from src.game.GameBoard import GameBoard


class Player:
    nickname = None
    position = None
    reserved_cards = None
    purchased_cards = None
    owned_tiles = None
    bank = None

    def __init__(self):
        self.purchased_cards = []
        self.reserved_cards = []
        self.owned_tiles = []
        self.bank = []
        self.position = None
        self.nickname = None

        for type in GameBoard.getTypes():
            self.bank.append(self.init_bank(type))

    def init_bank(self, type):
        tkStack = TokenStack(type)
        tkStack.set_type(type)
        tkStack.set_nb_token(0)
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

    def purchase_card(self, card):
        None