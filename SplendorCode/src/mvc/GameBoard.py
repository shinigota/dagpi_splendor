from src.element.RessourceType import RessourceType
from src.element.Token import Token
from src.game.GameState import GameState
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
    nb_players = 4
    ask_purchase_or_reserve_card = None
    display = None
    gamerules = None
    gamestate = None

    decks = None
    displayed_cards = None
    hidden_tiles = None
    displayed_tiles = None

    def __init__(self, display, gamerules):
        # Todo : init players, current_player, bank
        self.players = []
        self.gamerules = gamerules
        self.display = display
        self.types = []
        self.gamestate = GameState.PLAYER_TURN
        self.nb_gems = 2
        self.ask_purchase_or_reserve_card = False

        if self.nb_players == 2:
            self.nb_gems = self.gamerules.nb_gem_for_2
        elif self.nb_players == 3:
            self.nb_gems = self.gamerules.nb_gem_for_3
        else:
            self.nb_gems = self.gamerules.nb_gem_for_4

        self.init_bank()

        self.hidden_tiles = []
        self.displayed_tiles = []

        self.decks = dict(list)
        self.init_decks()
        self.displayed_cards = dict(list)

    # GameBoard init methods

    def init_gameboard(self):
        self.init_bank()
        self.init_decks()
        self.init_displayed_cards()
        self.init_tiles()

    def init_bank(self):
        self.bank = []
        for token_type in RessourceType.ressource_type.keys():
            self.bank[token_type] = self.nb_gems

    def init_decks(self):
        self.decks = []
        development_cards = self.gamerules.get_development_cards()
        for i in range(1, self.gamerules.nb_lvl_card):
            self.decks[i] = development_cards[i]

    def init_displayed_cards(self):
        self.displayed_cards = {}
        for i in range(1, self.gamerules.nb_lvl_card):
            self.fill_displayed_cards_lvl(i)

    def fill_displayed_cards_lvl(self, lvl):
        for i in range (1, 4):
            new_card = random.choice(self.decks[lvl])
            self.decks[lvl].remove(new_card)
            self.displayed_cards[int(lvl)].append(new_card)

    def init_tiles(self):
        self.hidden_tiles = []
        for i in range(1, self.nb_players + self.gamerules.nb_tile_more)
            tile = random.choice(self.hidden_tiles)
            self.hidden_tiles.remove(tile)
            self.displayed_tiles.append(tile)
            
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

    # Actions triggered by events

    def click_token_gameboard(self, token):
        """
        Action click on a gameboard's token
        :param token: gameboard's token which has been clicked
        :return: None
        """
        self.get_current_player().add_specific_token(token)
        self.bank[token.type] -= 1

        if self.get_current_player().is_action_complete():
            # self.end_action()
            if self.check_tokens_amount():
                self.gamestate = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.end_action()
                # next turn

    def click_token_player(self, token):
        """
        Action click on the player's token
        :param token:  player's token which has been clicked
        :return:
        """
        self.get_current_player().remove_specific_token(token)
        self.bank[token.type] += 1

        if self.get_current_player().is_action_complete():
            # self.end_action()
            if self.check_tokens_amount():
                self.gamestate = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                self.end_action()
                # display.update_view()

    def click_displayed_card(self, card):
        """
        Action click on a displayed card on the gameboard (ask purchase or
        reserve card)
        :param card:  Gameboard's displayed card clicked
        :return:
        """
        self.gamestate = GameState.PLAYER_CHOOSE_PURHCASE_OR_RESERVE

    def click_deck_card(self, card):
        """
        Action click on a deck's card
        :param card: deck's card which has been clicked
        :return:
        """
        self.get_current_player().add_reserved_card(card)
        # remove from deck

        if self.get_current_player().is_action_complete():
            # self.end_action()
            if self.check_tokens_amount():
                self.gamestate = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                # display.update_view()

    def click_purchase_card(self, card):
        '''
        Action purchase a previously selected card
        :param card: Card to purchase
        :return:
        '''
        self.replace_displayed_card(card)
        self.get_current_player().add_purchased_card(card)
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
        if self.get_current_player().is_action_complete():
            # self.end_action()
            if self.check_tokens_amount():
                self.gamestate = GameState.PLAYER_GIVE_TOKENS_BACK
            else:
                self.check_tiles()
                # display.update_view()

    def click_tile(self, tile):
        '''
        Action user clicks on some available tiles
        :param tile: Tile clicked
        :return:
        '''
        self.get_current_player().add_owned_tile(tile)
        if self.get_current_player().is_action_complete():
            self.end_action()

    # Game engine actions

    def end_action(self):
        self.get_current_player().init_turn()
        self.gamestate = GameState.PLAYER_TURN
        self.current_player += 1

    def check_tiles(self):
        tiles = []
        for tile in self.tiles:
            if self.check_enough_ressources(tile):
                tiles.append(tile)
        if len(tiles) > 1:
            self.gamestate = GameState.PLAYER_CHOOSE_TILE
            return True
        if len(tiles) == 1:
            tile.visit_player(self.get_current_player())
        return False

    # Getters

    def get_current_player(self):
        return self.players[self.current_player]

    def get_bank(self):
        return self.bank
