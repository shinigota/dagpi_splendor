from src.element.RessourceType import RessourceType
from src.element.Token import Token
from src.mvc.GameRules import GameRules
import random


def purchase_card(card):
    None
    # player.purchase_card(card)
    # add new card to gameboard, delete one from stack

    # display.update()


class GameBoard:
    players = None
    current_player = None
    bank = None
    nb_gems = None
    ask_purchase_or_reserve_card = None

    def __init__(self):
        # Todo : init players, current_player, bank
        self.players = []
        gameRules = GameRules()
        self.types = []
        nbPlayers = 0
        nb_gems = 2
        ask_purchase_or_reserve_card = False

        if nbPlayers == 2:
            nb_gems = gameRules.nb_gem_for_2
        elif nbPlayers == 3:
            nb_gems = gameRules.nb_gem_for_3
        else:
            nb_gems = gameRules.nb_gem_for_4

        self.init_bank()

        self.hidden_tiles = []
        self.displayed_tiles = []
        self.deck = dict(list)
        self.displayed_cards = dict(list)


    def add_type(self, type):
        self.types.append(type)

    def del_types(self, type):
        self.types.remove(type)
        del type

    def count_types(self):
        return len(self.types)

    def add_hidden_tile(self, tile):
        self.hidden_tiles.append(tile)

    def del_hidden_tile(self, tile):
        self.hidden_tiles.remove(tile)

    def add_displayed_tile(self, tile):
        self.displayed_tiles.append(tile)

    def del_displayed_tile(self, tile):
        self.displayed_tiles.remove(tile)

    def add_to_deck(self, card):
        self.deck[card.get_level()].append(card)

    def del_do_deck(self, card):
        self.deck[card.get_level()].remove(card)

    def add_displayed_card(self, card):
        self.displayed_cards[card.get_level()].append(card)

    def del_displayed_card(self, card):
        self.displayed_cards[card.get_level()].remove(card)

    def replace_displayed_card(self, card):
        lvl = card.get_level()
        loc = self.displayed_cards[lvl].index(card)
        self.displayed_cards[lvl].remove(card)

        new_card = random.choice(self.deck[int(lvl)])
        self.displayed_cards[int(lvl)].insert(loc, new_card)


    def init_bank(self):
        for token_type, token_color in RessourceType.ressource_type:
            self.bank[token_type] = self.nb_gems

    def fill_displayed_cards(self, lvl):
        new_card = random.choice(self.deck[int(lvl)])
        self.displayed_cards[int(lvl)].append(new_card)


    # Actions triggered by events

    def click_token_gameboard(self, token):
        """
        Action click on a gameboard's token
        :param token: gameboard's token which has been clicked
        :return: None
        """
        self.get_current_player().add_specific_token(token)
        self.bank[token.type] -= 1

        if self.get_current_player().is_turn_complete():
            self.next_turn()

    def click_token_player(self, token):
        """
        Action click on the player's token
        :param token:  player's token which has been clicked
        :return:
        """
        self.get_current_player().remove_specific_token(token)
        self.bank[token.type] += 1

        if self.get_current_player().is_turn_complete():
            self.next_turn()

        # display.update_view()

    def click_displayed_card(self, card):
        """
        Action click on a displayed card on the gameboard (ask purchase or
        reserve card)
        :param card:  Gameboard's displayed card clicked
        :return:
        """
        self.ask_purchase_or_reserve_card = True

    def click_deck_card(self, card):
        """
        Action click on a deck's card
        :param card: deck's card which has been clicked
        :return:
        """
        self.get_current_player().add_reserved_card(card)
        # remove from deck

        if self.get_current_player().is_turn_complete():
            self.next_turn()

        # display.update_view()

    def click_purchase_card(self, card):
        '''
        Action purchase a previously selected card
        :param card: Card to purchase
        :return:
        '''
        self.replace_displayed_card(card)
        if self.get_current_player().is_turn_complete():
            self.next_turn()
        # display.update_view()

    def click_reserve_card(self, card):
        '''
        Action reserve a previously selected card
        :param card: Card to reserve
        :return:
        '''
        self.get_current_player().add_reserved_card(card)
        if self.get_current_player().is_turn_complete():
            self.next_turn()
        # display.update_view()

    def click_tile(self, tile):
        '''
        Action user clicks on some available tiles
        :param tile: Tile clicked
        :return:
        '''
        self.get_current_player().add_owned_tile(tile)
        if self.get_current_player().is_turn_complete():
            self.next_turn()

    # Game engine actions

    def next_turn(self):
        self.ask_purchase_or_reserve_card = False

    # Getters

    def get_current_player(self):
        return self.players[self.current_player]

    def get_bank(self):
        return self.bank
