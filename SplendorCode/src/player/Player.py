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
    # Turn verification values
    tokens_took = None
    purchased_card_amount = None
    reserved_card_amount = None

    def __init__(self, nickname, position):
        self.purchasedCards = [Card]
        self.reservedCards = [Card]
        self.ownedTiles = [Tile]
        self.bank = [Token]
        self.position = position
        self.nickname = nickname
        self.init_turn()

    def init_bank(self):
        for ressource_type, ressource in RessourceType.ressource_type.items():
            self.bank[ressource_type] = 0

    def add_purchased_card(self, card):
        self.purchased_cards.append(card)
        self.purchased_card_amount += 1

    def add_reserved_card(self, card):
        self.reserved_cards.append(card)
        self.reserved_card_amount += 1

    def del_reserved_card(self, card):
        self.reserved_cards.remove(card)

    def add_owned_tile(self, tile):
        self.owned_tiles.append(tile)

    def add_different_tokens(self, tokens):
        for tokenType, token_amount in tokens:
            self.bank[tokenType] += token_amount
            self.tokens_took[tokenType] += token_amount

    def add_specific_token(self, token_type, number=1):
        self.bank[token_type] += number
        self.tokens_took[token_type] += number

    def remove_different_tokens(self, tokens):
        for tokenType, token_amount in tokens:
            self.bank[tokenType] -= token_amount
            self.tokens_took[tokenType] -= token_amount

    def remove_specific_token(self, token_type, number=1):
        self.bank[token_type] -= number
        self.tokens_took[token_type] -= number

    def init_turn(self):
        self.tokens_took = {}
        self.purchased_card_amount = 0
        self.reserved_card_amount = 0

    def is_action_complete(self):
        return (self.token_choice_valid() or
                self.purchased_card_amount == 1 or
                self.reserved_card_amount == 1)

    def token_choice_valid(self):
        tokens_amount = sum(self.tokens_took.values())
        if tokens_amount == 2:
            return 2 not in self.tokens_took.values()
        elif tokens_amount == 3:
            return (2 not in self.tokens_took.values() and
                    3 not in self.tokens_took.values())
        return False
