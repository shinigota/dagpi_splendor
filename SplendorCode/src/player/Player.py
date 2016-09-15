from copy import copy

from src.element.Card import Card
from src.element.ResourceType import ResourceType
from src.element.Tile import Tile
from src.element.Token import Token
from src.game.GameState import GameState
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
        print('Player -- init_bank')
        self.bank = {}
        for resource_type, resource in ResourceType.resource_type.items():
            self.bank[resource_type] = 0

    def init_purchased_cards(self):
        print('Player -- init_purchased_cards')
        self.purchased_cards = {}
        for resource_type, resource in ResourceType.resource_type.items():
            if resource_type != "Gold":
                '''self.purchased_cards[resource_type] = [Card(0,
                                                            resource_type,
                                                            {
                                                                "Emerald": 0,
                                                                "Diamond": 0,
                                                                "Sapphire": 0,
                                                                "Onyx": 0,
                                                                "Ruby": 0
                                                            },
                                                            1),
                                                       Card(0,
                                                            resource_type,
                                                            {
                                                                "Emerald": 0,
                                                                "Diamond": 0,
                                                                "Sapphire": 0,
                                                                "Onyx": 0,
                                                                "Ruby": 0
                                                            },
                                                            1),
                                                       Card(0,
                                                            resource_type,
                                                           {
                                                                "Emerald": 0,
                                                                "Diamond": 0,
                                                                "Sapphire": 0,
                                                                "Onyx": 0,
                                                                "Ruby": 0
                                                            },
                                                            1),
                                                       Card(0,
                                                            resource_type,
                                                            {
                                                                "Emerald": 0,
                                                                "Diamond": 0,
                                                                "Sapphire": 0,
                                                                "Onyx": 0,
                                                                "Ruby": 0
                                                            },
                                                            1),
                                                       ]'''
                self.purchased_cards[resource_type] = []

                #self.purchased_cards[resource_type] = []

    def add_purchased_card(self, card):
        print('Player -- add_purchased_card')
        self.purchased_cards[card.get_income_gem()].append(card)
        self.purchased_card_amount += 1

    def add_reserved_card(self, card):
        print('Player -- add_reserved_card')
        self.reserved_cards.append(card)
        self.reserved_card_amount += 1

    def del_reserved_card(self, card):
        print('Player -- del_reserved_card')
        self.reserved_cards.remove(card)
        self.reserved_card_amount -= 1

    def add_owned_tile(self, tile):
        print('Player -- add_owned_tile')
        self.owned_tiles.append(tile)

    def add_different_tokens(self, tokens):
        print('Player -- add_different_tokens')
        for tokenType, token_amount in tokens:
            self.bank[tokenType] += token_amount
            self.tokens_took[tokenType] += token_amount

    def add_specific_token(self, token_type, number=1):
        print('Player -- add_specific_token')
        self.bank[token_type] += number
        self.tokens_took[token_type] += number

    def remove_different_tokens(self, tokens):
        print('Player -- remove_different_tokens')
        amount_gold_removed = 0
        for resource_type, amount in tokens.items():
            self.bank[resource_type] -= amount
            if resource_type == "Gold":
                amount_gold_removed += amount
        return amount_gold_removed

    def get_tokens_to_spend(self, tokens):
        print("Player -- get_tokens_to_spend")
        token_copy = copy(tokens)
        token_copy["Gold"] = 0

        card_income = self.get_card_income()
        for token_type in token_copy.keys():
            if token_type == "Gold":
                continue
            if token_copy[token_type] > 0:
                token_copy[token_type] = max(token_copy[token_type] - card_income[
                    token_type], 0)
            if self.bank[token_type] < token_copy[token_type] and \
                    token_copy[token_type] > 0:
                delta = token_copy[token_type] - self.bank[token_type]
                token_copy["Gold"] += delta
                token_copy[token_type] -= delta

        return token_copy

    def remove_specific_token(self, token_type, number=1):
        print('Player -- remove_specific_token')
        self.bank[token_type] -= number
        self.tokens_took[token_type] -= number

    def init_turn(self):
        print('Player -- init_turn')
        self.tokens_took = {}
        for resource_type in ResourceType.resource_type:
            self.tokens_took[resource_type] = 0
        self.purchased_card_amount = 0
        self.reserved_card_amount = 0

    def is_action_complete(self, game_state):
        print('Player -- is_action_complete')
        val = (self.token_choice_valid() or
                self.purchased_card_amount >= 1 or
                self.reserved_card_amount >= 1
                or game_state == GameState.PLAYER_GIVE_TOKENS_BACK)
        return val

    def token_choice_valid(self):
        print('Player -- token_choice_valid')
        tokens_amount = sum(self.tokens_took.values())
        if tokens_amount == 2:
            return 2 in self.tokens_took.values()
        elif tokens_amount == 3:
            return (2 not in self.tokens_took.values() and
                    3 not in self.tokens_took.values())
        return tokens_amount <= 0

    def calculate_total_points(self):
        print('Player -- calculate_total_points')
        nb_points = 0
        for card_type, cards in self.purchased_cards.items():
            for card in cards:
                nb_points += card.points

        for ptile in self.owned_tiles:
            nb_points += ptile.points

        return nb_points

    def can_reserve_card(self):
        print('Player -- can_reserve_card')
        return len(self.reserved_cards) < GameRules.nb_max_res_card and sum(
            self.tokens_took.values()) == 0

    def get_card_income(self):
        print('Player -- get_card_income')
        income = {}
        for resource_type in ResourceType.resource_type.keys():
            if resource_type != "Gold":
                income[resource_type] = 0

        for card_type, cards in self.purchased_cards.items():
            income[card_type] += len(cards)

        return income

    def get_income(self):
        print('Player -- get_income')
        income = self.bank.copy()
        for resource_type, amount in self.get_card_income().items():
            income[resource_type] += amount

        return income

    def play(self):
        print('Player -- play')
        pass
