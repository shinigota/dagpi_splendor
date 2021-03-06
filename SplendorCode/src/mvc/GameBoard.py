import time

import sys
from copy import deepcopy

from src.element.ResourceType import ResourceType
from src.game.GameState import GameState
from src.game.GameStateString import GameStateString
from src.mvc.GameRules import GameRules
import random

from src.player.Player import Player


class GameBoard:
    players = None
    current_player = None
    bank = None
    nb_gems = None
    nb_players = 1
    ask_purchase_or_reserve_card = None
    display = None
    game_rules = None
    game_state = None
    human_player = None
    decks = None
    displayed_cards = None
    hidden_tiles = None
    displayed_tiles = None
    end_game = None
    winners = None
    help_text = None
    parameters = None

    def __init__(self, display, game_rules):
        self.game_rules = game_rules
        self.display = display

    # game_board init methods

    def init_parameters(self, parameters):
        print('GameBoard -- init_parameters')
        self.nb_players = len(parameters)
        print(self.nb_players)
        print(parameters)
        self.parameters = parameters

    def start_game(self):
        print('GameBoard -- start_game')
        self.init_game_board()
        self.display.refresh()
        self.get_current_player().play()

    def init_game_board(self):
        """
        game_board initialization / creation, adding the cards / tokens to
        the board
        :return:
        """
        print('GameBoard -- init_game_board')
        self.types = []
        self.game_state = GameState.PLAYER_TURN
        self.nb_gems = 2

        if self.nb_players == 2:
            self.nb_gems = self.game_rules.nb_gem_for_2
        elif self.nb_players == 3:
            self.nb_gems = self.game_rules.nb_gem_for_3
        else:
            self.nb_gems = self.game_rules.nb_gem_for_4

        self.help_text = ""
        self.end_game = False
        self.winners = []

        self.init_bank()
        self.init_cards()
        self.init_tiles()
        self.init_players()

    def init_bank(self):
        """
        Initialising the bank, creating the tokens
        :return:
        """
        print('GameBoard -- init_bank')
        self.bank = {}
        for token_type in ResourceType.resource_type.keys():
            nb = int(self.nb_gems)
            if token_type == "Gold":
                nb = GameRules.nb_gold
            self.bank[token_type] = nb

    def init_cards(self):
        """
        Initialising the 3 different level of cards
        :return:
        """
        print('GameBoard -- init_cards')
        self.decks = {}
        development_cards = self.game_rules.get_development_cards()
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            self.decks[i] = development_cards[i]
            print('GameBoard -- init_cards FOR')
        print(self.decks)
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
        print('GameBoard -- init_tiles')
        self.hidden_tiles = self.game_rules.get_tiles()
        self.displayed_tiles = []
        for i in range(1, self.nb_players + int(GameRules.nb_tile_more) + 1):
            tile = random.choice(self.hidden_tiles)
            self.hidden_tiles.remove(tile)
            self.displayed_tiles.append(tile)

    def init_players(self):
        print('GameBoard -- init_players')
        self.players = []
        self.players.append(Player(self.parameters[0]["name"],
                                   self.parameters[0]["position"]))
        self.human_player = self.players[0]

        for i in range(1, self.nb_players):
            from src.player.AI import AI
            self.players.append(
                AI(self.parameters[i]["name"], self.parameters[i]["position"],
                   self.parameters[i]["difficulty"], self, self.game_rules))
        self.current_player = 0

        self.players.sort(key=lambda x: int(x.position), reverse=False)

        self.help_text = GameStateString.get_text(GameState.PLAYER_TURN,
                                                  self.get_current_player().nickname)

    # Actions triggered by events

    def click_token_game_board(self, token):
        """
        Action click on a game_board's token
        :param token: game_board's token which has been clicked
        :return: None
        """
        print('GameBoard -- click_token_game_board')
        print(self.player_can_play())
        self.get_current_player().add_specific_token(token)
        self.bank[token] -= 1

        if self.get_current_player().is_action_complete(self.game_state) or \
                not self.can_take_token():
            if self.check_tokens_amount():
                print(
                    '-------\n-------\n-------\n-------\n-------\n-------\n-------\n-------\n-------\n-------\n-------')
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
                self.help_text = GameStateString.get_text(
                    GameState.PLAYER_GIVE_TOKENS_BACK,
                    self.get_current_player().nickname)
            else:
                self.check_tiles()
        self.display.refresh()

    def click_token_player(self, token):
        """
        Action click on the player's token
        :param token:  player's token which has been clicked
        :return:
        """
        print('GameBoard -- click_token_player')
        print(self.player_can_play())
        self.get_current_player().remove_specific_token(token)
        self.bank[token] += 1

        if self.get_current_player().is_action_complete(self.game_state):
            if self.check_tokens_amount():
                print(
                    '111111\n111111\n111111\n111111\n111111\n')
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
                self.help_text = GameStateString.get_text(
                    GameState.PLAYER_GIVE_TOKENS_BACK,
                    self.get_current_player().nickname)
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
        print('GameBoard -- click_displayed_cards')
        self.game_state = GameState.PLAYER_CHOOSE_PURHCASE_OR_RESERVE

    def click_deck_card(self, lvl):
        """
        Action click on a deck's card
        :param lvl: lvl of the clicked deck
        :return:
        """
        print('GameBoard -- click_deck_card')
        card = self.choose_card_in_deck(lvl)
        self.get_current_player().add_reserved_card(card)
        self.add_gold_to_player()

        # remove from deck

        if self.get_current_player().is_action_complete(self.game_state):
            if self.check_tokens_amount():
                print(
                    '22222\n22222\n22222\n22222\n22222\n')
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
                self.help_text = GameStateString.get_text(
                    GameState.PLAYER_GIVE_TOKENS_BACK,
                    self.get_current_player().nickname)
            else:
                self.check_tiles()

        self.display.refresh()

    def click_purchase_gameboard_card(self, card):
        '''
        Action purchase a previously selected card
        :param card: Card to purchase
        :return:
        '''
        print("GameBoard -- click_purchase_gameboard_card")
        print(self.get_current_player().nickname)
        print(card)
        self.replace_displayed_card(card)
        self.get_current_player().add_purchased_card(card)
        cost = self.get_current_player().get_tokens_to_spend(
            card.get_purchase_gems())
        self.get_current_player().remove_different_tokens(cost)
        self.add_to_bank(cost)
        if self.get_current_player().is_action_complete(self.game_state):
            self.check_tiles()
        self.display.refresh()

    def click_purchase_reserve_card(self, card):
        '''
        Action purchase a previously selected card
        :param card: Card to purchase
        :return:
        '''
        print("GameBoard -- click_purchase_reserve_card")
        print(self.get_current_player().nickname)
        print(card)
        self.get_current_player().reserved_cards.remove(card)
        self.get_current_player().add_purchased_card(card)
        cost = self.get_current_player().get_tokens_to_spend(
            card.get_purchase_gems())
        self.get_current_player().remove_different_tokens(cost)
        self.add_to_bank(cost)
        if self.get_current_player().is_action_complete(self.game_state):
            if self.check_tokens_amount():
                print(
                    '44444\n44444\n44444\n44444\n44444\n')
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
        self.display.refresh()

    def click_reserve_card(self, card):
        '''
        Action reserve a previously selected card
        :param card: Card to reserve
        :return:
        '''
        print('GameBoard -- click_reserve_card')
        self.replace_displayed_card(card)
        self.get_current_player().add_reserved_card(card)
        self.add_gold_to_player()

        if self.get_current_player().is_action_complete(self.game_state):
            if self.check_tokens_amount():
                self.game_state = GameState.PLAYER_GIVE_TOKENS_BACK
                self.help_text = GameStateString.get_text(
                    GameState.PLAYER_GIVE_TOKENS_BACK,
                    self.get_current_player().nickname)
            else:
                self.check_tiles()

        self.display.refresh()

    def click_tile(self, tile):
        '''
        Action user clicks on some available tiles
        :param tile: Tile clicked
        :return:
        '''
        print('GameBoard -- click_tile')
        self.del_displayed_tile(tile)
        self.get_current_player().add_owned_tile(tile)
        # self.displayed_tiles.remove(tile)
        if self.get_current_player().is_action_complete(self.game_state):
            self.end_action()
        self.display.refresh()

    # Game engine actions

    def check_winner(self):
        print('GameBoard -- check_winner')
        if self.get_current_player().calculate_total_points() >= GameRules.nb_points_end:
            return True
        return False

    def end_action(self):
        print('GameBoard -- end_action')
        if self.check_winner():
            self.end_game = True
            self.winners.append(self.get_current_player())
        self.get_current_player().init_turn()
        self.game_state = GameState.PLAYER_TURN
        self.current_player = (self.current_player + 1) % self.nb_players
        if self.current_player == 0 and self.end_game:
            self.sort_players_end()
            winner_popup_text = "Classement des joueurs : "
            for winning_player in self.winners:
                winner_popup_text += "\n%s : %d" % (
                    winning_player.nickname,
                    winning_player.calculate_total_points())
            self.display.popup_txt(winner_popup_text)

        self.help_text = GameStateString.get_text(GameState.PLAYER_TURN,
                                                  self.get_current_player().nickname)

        if not self.player_can_play():
            self.end_action()
        # self.get_current_player().action_AI_basic()
        else:
            from src.player.AI import AI
            self.get_current_player().play()

    def sort_players_end(self):
        print('GameBoard -- sort_player_end')
        self.winners.sort(key=lambda x: x.calculate_total_points(),
                          reverse=True)
        missing_players = []
        for player in self.players:
            if player not in self.winners:
                missing_players.append(player)

        missing_players.sort(key=lambda x: x.calculate_total_points(),
                             reverse=True)

        self.winners.extend(missing_players)

    def check_tiles(self):
        print("GameBoard -- check_tiles")
        self.tiles = []
        for tile in self.displayed_tiles:
            if self.check_enough_cards(tile):
                self.tiles.append(tile)
        if len(self.tiles) > 1:
            self.game_state = GameState.PLAYER_CHOOSE_TILE
            self.display.popup_select_tile_action(self.tiles)
            return True
        if len(self.tiles) == 1:
            self.tiles[0].visit_player(self.get_current_player())
            self.displayed_tiles.remove(self.tiles[0])
            self.tiles.pop(0)
        self.end_action()
        return False

    # tuile
    def check_enough_cards(self, tile):
        print('GameBoard -- check_enough_cards')
        for required_gem, \
            required_amount \
                in tile.gems_conditions.items():
            player_gem_amount = 0
            for tmp_cards in self.get_current_player().purchased_cards.values():
                for tmp_card in tmp_cards:
                    if tmp_card.get_income_gem() == required_gem:
                        player_gem_amount += 1
            if required_amount > player_gem_amount:
                return False

        return True

    def check_tokens_amount(self):
        print('GameBoard -- check_tokens_amount')
        nb_token = sum(v for v in self.get_current_player().bank.values())
        return nb_token > GameRules.nb_token_end_turn

    # functions

    def add_to_bank(self, tokens):
        print('GameBoard -- add_to_bank')
        for resource_type, amount in tokens.items():
            self.bank[resource_type] += amount

    def add_type(self, type):
        print('GameBoard -- add_type')
        self.types.append(type)

    def del_types(self, type):
        print('GameBoard -- del_types')
        self.types.remove(type)
        del type

    def add_hidden_tile(self, tile):
        print('GameBoard -- add_hidden_tiles')
        self.hidden_tiles.append(tile)

    def del_hidden_tile(self, tile):
        print('GameBoard -- del_hidden_tiles')
        self.hidden_tiles.remove(tile)

    def add_displayed_tile(self, tile):
        print('GameBoard -- add_displayed_tiles')
        self.displayed_tiles.append(tile)

    def del_displayed_tile(self, tile):
        print('GameBoard -- del_displayed_tiles')
        self.displayed_tiles.remove(tile)

    def add_to_deck(self, card):
        print('GameBoard -- add_to_deck')
        self.decks[card.get_level()].append(card)

    def del_do_deck(self, card):
        print('GameBoard -- del_to_deck')
        self.decks[card.get_level()].remove(card)

    def choose_card_in_deck(self, lvl):
        print('GameBoard -- choose_card_in_deck')
        new_card = random.choice(self.decks[int(lvl)])
        self.decks[int(lvl)].remove(new_card)
        return new_card

    def add_displayed_card(self, card):
        print('GameBoard -- add_displayed_card')
        self.displayed_cards[card.get_level()].append(card)

    def del_displayed_card(self, card):
        print('GameBoard -- del_displayed_card')
        self.displayed_cards[card.get_level()].remove(card)

    def replace_displayed_card(self, card):
        print('GameBoard -- replace_displayed_card')
        lvl = card.get_level()
        loc = self.displayed_cards[lvl].index(card)
        self.displayed_cards[lvl].remove(card)

        if len(self.decks[int(lvl)]) != 0:
            new_card = self.choose_card_in_deck(lvl)
            self.displayed_cards[int(lvl)].insert(loc, new_card)

    def fill_displayed_cards(self, lvl):
        print('GameBoard -- fill_displayed_cards')
        new_card = self.choose_card_in_deck(lvl)
        self.displayed_cards[int(lvl)].append(new_card)

    def is_deck_empty(self, lvl):
        print('GameBoard -- is_deck_empty')
        if len(self.decks[int(lvl)]) == 0:
            return True
        else:
            return False

    def can_take_token(self):
        print('GameBoard -- can_take_token')
        for token, amount in self.bank.items():
            if amount > 0 and token != "Gold":
                if self.get_current_player().tokens_took[token] == 0:
                    return True
                elif self.get_current_player().tokens_took[token] < 2 and \
                                amount >= 3:
                    return True
        return False

    def add_gold_to_player(self):
        print('GameBoard -- add_gold_to_player')
        if self.bank["Gold"] > 0:
            self.get_current_player().bank["Gold"] += 1
            self.bank["Gold"] -= 1

    def player_can_play(self):
        print('GameBoard -- player_can_play')
        player = self.get_current_player()

        number_cards_deck = 0
        for deck in self.decks.items():
            print(deck)
            number_cards_deck += len(deck)

        if player.can_reserve_card() and number_cards_deck < GameRules.nb_max_res_card:
            return True

        for cards_from_lvl in self.displayed_cards.values():
            for card in cards_from_lvl:
                if card.is_purchasable(player.get_income()):
                    return True

        possible_resources = 0
        for token_type, token_amount in self.bank.items():
            if token_type != "Gold" and token_amount >= 4:
                return True

            if token_type != "Gold" and token_amount >= 1:
                possible_resources += 1

            if possible_resources >= GameRules.nb_gem_diff - sum(self.get_current_player().tokens_took.values()):
                return True

        return False

    # Getters

    def get_current_player(self):
        print('GameBoard -- get_current_player')
        return self.players[self.current_player]

    def get_bank(self):
        print('GameBoard -- get_bank')
        return self.bank

    def get_human_player(self):
        print('GameBoard -- get_human_player')
        return self.human_player

    def get_game_state(self):
        print('GameBoard -- get_game_state')
        return self.game_state
