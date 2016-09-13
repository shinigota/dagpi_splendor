from src.element.ResourceType import ResourceType
from src.game.GameState import GameState
from src.mvc.GameRules import GameRules
import random

from src.player.Player import Player


class GameBoard:
    players = None
    current_player = None
    bank = None
    nb_gems = None
    nb_players = 4
    ask_purchase_or_reserve_card = None
    display = None
    game_rules = None
    game_state = None

    decks = None
    displayed_cards = None
    hidden_tiles = None
    displayed_tiles = None

    def __init__(self, display, game_rules):
        self.game_rules = game_rules
        self.display = display
        self.types = []
        self.game_state = GameState.PLAYER_TURN
        self.nb_gems = 2

        if self.nb_players == 2:
            self.nb_gems = self.game_rules.nb_gem_for_2
        elif self.nb_players == 3:
            self.nb_gems = self.game_rules.nb_gem_for_3
        else:
            self.nb_gems = self.game_rules.nb_gem_for_4

        self.init_game_board()

    # game_board init methods

    def init_game_board(self):
        """
        game_board initialization / creation, adding the cards / tokens to
        the board
        :return:
        """
        self.init_bank()
        self.init_cards()
        self.init_tiles()
        self.init_players()

    def init_bank(self):
        """
        Initialising the bank, creating the tokens
        :return:
        """
        self.bank = {}
        for token_type in ResourceType.resource_type.keys():
            nb = self.nb_gems
            if token_type == "Gold":
                nb = GameRules.nb_gold
            self.bank[token_type] = nb

    def init_cards(self):
        """
        Initialising the 3 different level of cards
        :return:
        """
        self.decks = {}
        development_cards = self.game_rules.get_development_cards()
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            self.decks[i] = development_cards[i]

        self.displayed_cards = {}
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            self.displayed_cards[i] = []
            for x in range(1, int(self.game_rules.nb_card_reveal) + 1):
                self.fill_displayed_cards(i)

    def init_tiles(self):
        """
        Initialising the available and hidden tiles
        :return:
        """
        self.hidden_tiles = self.game_rules.get_tiles()
        self.displayed_tiles = []
        for i in range(1, self.nb_players + int(GameRules.nb_tile_more) + 1):
            tile = random.choice(self.hidden_tiles)
            self.hidden_tiles.remove(tile)
            self.displayed_tiles.append(tile)

    def init_players(self):
        self.players = []
        for i in range(0, self.nb_players):
            self.players.append(Player("Joueur %d" % i, i + 1))
        self.current_player = 0
        self.get_current_player().add_reserved_card(self.displayed_cards[1][1])
        self.get_current_player().add_reserved_card(self.displayed_cards[2][1])
        self.get_current_player().add_reserved_card(self.displayed_cards[3][1])

    # Actions triggered by events

    def click_token_game_board(self, token):
        """
        Action click on a game_board's token
        :param token: game_board's token which has been clicked
        :return: None
        """
        self.get_current_player().add_specific_token(token)
        self.bank[token.type] -= 1

        if self.get_current_player().is_action_complete():
            if self.check_tokens_amount():
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.display.refresh()

    def click_token_player(self, token):
        """
        Action click on the player's token
        :param token:  player's token which has been clicked
        :return:
        """
        self.get_current_player().remove_specific_token(token)
        self.bank[token.type] += 1

        if self.get_current_player().is_action_complete():
            if self.check_tokens_amount():
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.display.refresh()

    def click_displayed_card(self, card):
        """
        Action click on a displayed card on the game_board (ask purchase or
        reserve card)
        :param card:  Gameboard's displayed card clicked
        :return:
        """
        self.game_state = GameState.PLAYER_CHOOSE_PURHCASE_OR_RESERVE

    def click_deck_card(self, lvl):
        """
        Action click on a deck's card
        :param lvl: lvl of the clicked deck
        :return:
        """
        card = self.choose_card_in_deck(lvl)
        self.get_current_player().add_reserved_card(card)
        # remove from deck

        if self.get_current_player().is_action_complete():
            if self.check_tokens_amount():
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.display.refresh()

    def click_purchase_card(self, card):
        '''
        Action purchase a previously selected card
        :param card: Card to purchase
        :return:
        '''
        self.replace_displayed_card(card)
        self.get_current_player().add_purchased_card(card)
        if self.get_current_player().is_turn_complete():
            self.check_tiles()
            self.display.refresh()

    def click_reserve_card(self, card):
        '''
        Action reserve a previously selected card
        :param card: Card to reserve
        :return:
        '''
        self.replace_displayed_card(card)
        self.get_current_player().add_reserved_card(card)
        self.get_current_player().add_specific_token("Gold",
                                                     GameRules.nb_gold_take)
        if self.get_current_player().is_action_complete():
            if self.check_tokens_amount():
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.display.refresh()

    def click_tile(self, tile):
        '''
        Action user clicks on some available tiles
        :param tile: Tile clicked
        :return:
        '''
        self.del_displayed_tile(tile)
        self.get_current_player().add_owned_tile(tile)
        if self.get_current_player().is_action_complete():
            self.end_action()

    # Game engine actions

    def end_action(self):
        self.get_current_player().init_turn()
        self.game_state = GameState.PLAYER_TURN
        self.current_player = (self.current_player + 1) % self.nb_players

    def check_tiles(self):
        tiles = []
        for tile in self.displayed_tiles:
            if self.check_enough_cards(tile):
                tiles.append(tile)
        if len(tiles) > 1:
            self.game_state = GameState.PLAYER_CHOOSE_TILE
            return True
        if len(tiles) == 1:
            tiles[0].visit_player(self.get_current_player())
        self.end_action()
        return False

    # tuile
    def check_enough_cards(self, tile):
        for gem_player, val_player in self.get_current_player().purchased_cards.items:
            for gem_tile, val_tile in tile.gem_conditions.items:
                if gem_player == gem_tile:
                    if val_tile > val_player:
                        return False
        return True

    def check_tokens_amount(self):
        nb_token = sum(v for v in self.get_current_player().bank.values)
        if nb_token >= GameRules.nb_token_end_turn:
            return nb_token - GameRules.nb_token_end_turn
            # return True

    # functions

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
        self.decks[card.get_level()].append(card)

    def del_do_deck(self, card):
        self.decks[card.get_level()].remove(card)

    def choose_card_in_deck(self, lvl):
        new_card = random.choice(self.decks[int(lvl)])
        self.decks[int(lvl)].remove(new_card)
        return new_card

    def add_displayed_card(self, card):
        self.displayed_cards[card.get_level()].append(card)

    def del_displayed_card(self, card):
        self.displayed_cards[card.get_level()].remove(card)

    def replace_displayed_card(self, card):
        lvl = card.get_level()
        loc = self.displayed_cards[lvl].index(card)
        self.displayed_cards[lvl].remove(card)

        if len(self.decks[int(lvl)]) != 0:
            new_card = self.choose_card_in_deck(lvl)
            self.displayed_cards[int(lvl)].insert(loc, new_card)

    def fill_displayed_cards(self, lvl):
        new_card = random.choice(self.decks[int(lvl)])
        self.displayed_cards[int(lvl)].append(new_card)

    def is_deck_empty(self, lvl):
        if len(self.decks[int(lvl)]) == 0:
            return True
        else:
            return False

    # Getters

    def get_current_player(self):
        return self.players[self.current_player]

    def get_bank(self):
        return self.bank
