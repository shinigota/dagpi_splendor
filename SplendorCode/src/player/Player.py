from src.element.Card import Card
from src.element.ResourceType import ResourceType
from src.element.Tile import Tile
from src.element.Token import Token
from src.mvc.GameRules import GameRules


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
        self.position = position
        self.nickname = nickname
        self.reserved_cards = []
        self.owned_tiles = []
        self.init_bank()
        self.init_purchased_cards()
        self.init_turn()

    def init_bank(self):
        self.bank = {}
        for resource_type, resource in ResourceType.resource_type.items():
            self.bank[resource_type] = 1

    def init_purchased_cards(self):
        self.purchased_cards = {}
        for resource_type, resource in ResourceType.resource_type.items():
            if resource_type != "Gold":
                # self.purchased_cards[resource_type] = [Card(0,
                #                                             resource_type, {
                #                                                 "Emerald": 0,
                #                                                 "Diamond": 0,
                #                                                 "Sapphire": 0,
                #                                                 "Onyx": 0,
                #                                                 "Ruby": 0
                #                                             }, 1)]
                self.purchased_cards[resource_type] = []
    def add_purchased_card(self, card):
        self.purchased_cards[card.get_income_gem()].append(card)
        self.purchased_card_amount += 1

    def add_reserved_card(self, card):
        self.reserved_cards.append(card)
        self.reserved_card_amount += 1

    def del_reserved_card(self, card):
        self.reserved_cards.remove(card)
        self.reserved_card_amount -= 1

    def add_owned_tile(self, tile):
        self.owned_tiles.append(tile)

    def add_different_tokens(self, tokens):
        for tokenType, token_amount in tokens:
            self.bank[tokenType] += token_amount
            self.tokens_took[tokenType] += token_amount

    def add_specific_token(self, token_type, number=1):
        self.bank[token_type] += number
        self.tokens_took[token_type] += number

    def remove_different_tokens(self, tokens, use_card_income=False):
        available_gold = self.bank["Gold"]
        card_income = self.get_card_income()
        for token_type, token_amount in tokens.items():
            delta = token_amount
            if use_card_income:
                if card_income[token_type] + self.bank[token_type] + available_gold \
                        >= \
                        token_amount:
                    if token_amount - card_income[token_type] >= 0:
                        delta = token_amount - card_income[token_type]
            self.bank[token_type] -= delta
            self.tokens_took[token_type] -= delta

    def remove_specific_token(self, token_type, number=1):
        self.bank[token_type] -= number
        self.tokens_took[token_type] -= number

    def init_turn(self):
        self.tokens_took = {}
        for resource_type in ResourceType.resource_type:
            self.tokens_took[resource_type] = 0
        self.purchased_card_amount = 0
        self.reserved_card_amount = 0

    def is_action_complete(self):
        return (self.token_choice_valid() or
                self.purchased_card_amount >= 1 or
                self.reserved_card_amount >= 1)

    def token_choice_valid(self):
        tokens_amount = sum(self.tokens_took.values())
        if tokens_amount == 2:
            return 2 in self.tokens_took.values()
        elif tokens_amount == 3:
            return (2 not in self.tokens_took.values() and
                    3 not in self.tokens_took.values())
        return tokens_amount <= 0

    def calcul_point_in_game(self):
        nb_points = 0
        for card_type, cards in self.purchased_cards.items():
            for card in cards:
                nb_points += card.points

        for ptile in self.owned_tiles:
            nb_points += ptile.points

        return nb_points

    def can_reserve_card(self):
        return len(self.reserved_cards) < GameRules.nb_max_res_card and sum(
            self.tokens_took.values()) == 0

    def get_card_income(self):
        income = {}
        for resource_type in ResourceType.resource_type.keys():
            if resource_type != "Gold":
                income[resource_type] = 0

        for card_type, cards in self.purchased_cards.items():
            income[card_type] += len(cards)

        return income

    def get_income(self):
        income = self.bank.copy()
        for resource_type, amount in self.get_card_income().items():
            income[resource_type] += amount

        return income

    def action_AI_basic(self):
        pass