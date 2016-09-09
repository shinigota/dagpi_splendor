from src.element.Card import Card
from src.element.RessourceType import RessourceType
from src.element.Tile import Tile
from src.element.Token import Token


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
        self.bank = [Token]
        self.position = position
        self.nickname = nickname

    def init_bank(self):
        for ressourceType, ressource in RessourceType.ressource_type.items():
            self.bank[ressourceType] = 0

    def add_purchased_card(self, card):
        self.purchased_cards.append(card)

    def add_reserved_card(self, card):
        self.reserved_cards.append(card)

    def del_reserved_card(self, card):
        self.reserved_cards.remove(card)

    def add_owned_tile(self, tile):
        self.owned_tiles.append(tile)

    def add_different_tokens(self, tokens):
        for tokenType, tokenAmount in tokens:
            self.bank[tokenType] += tokenAmount

    def add_specific_token(self, tokenType, number=1):
        self.bank[tokenType] += number

    def remove_different_tokens(self, tokens):
        for tokenType, tokenAmount in tokens:
            self.bank[tokenType] -= tokenAmount

    def remove_specific_token(self, tokenType, number=1):
        self.bank[tokenType] -= number
