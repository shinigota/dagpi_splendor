from src.player.Player import Player
from src.mvc.EventType import EventType
from src.mvc import GameBoard
from src.mvc import GameRules
import random


class AI(Player):
    difficulty = None
    game_board = None
    game_rules = None
    game_state = None
    ressource = None

    def __init__(self, name, position, difficulty, game_board=None,
                 game_rules=None):
        Player.__init__(self, name, position)
        self.game_board = game_board
        self.game_rules = game_rules
        self.difficulty = difficulty
        self.position = position

    def action_AI_basic(self):

        l_action = ["two", "three", "reserved", "purchase"]
        bool_action = False

        while len(l_action) > 1 or not bool_action:
            action_ia = random.choice(list(l_action))

            if action_ia == "two":
                dict_t2 = {}
                for k, v in self.game_board.bank.items():
                    if v >= self.game_board.nb_min_gem_stack:
                        dict_t2[k] = v
                if len(dict_t2) == 0:
                    l_action.remove(action_ia)
                else:
                    token_t2 = random.choice(list(dict_t2.items()))
                    self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                          token_t2)
                    token_type_t2 = token_t2[1]
                    token_nb_t2 = token_t2[0]
                    token_t2 = (token_type_t2, token_nb_t2)
                    self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                          token_t2)
                    bool_action = True

            if action_ia == "three":
                dict_t3 = {}
                for k, v in self.game_board.bank.items():
                    if v > 0:
                        dict_t3[k] = v
                if len(dict_t3) < 3:
                    l_action.remove(action_ia)
                else:
                    for i in range(1, 4):
                        token_t3 = random.choice(list(dict_t3.items()))
                        token_type_t3 = token_t3[0]
                        self.game_rules.event(
                            EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token_type_t3)
                        del dict_t3[token_type_t3]
                    bool_action = True

            if action_ia == "reserved":
                while not bool_action:
                    if self.reserved_cards == self.game_rules.nb_max_res_card:
                        l_action.remove("reserved")
                        break
                    l_where_r = ["deck", "card"]
                    where_r = random.choice(list(l_where_r))
                    l_lvl = [1, 2, 3]
                    if where_r == "deck":
                        self.game_rules.event(EventType.CLICK_DECK_CARD,
                                              random.choice(list(l_lvl)))
                        bool_action = True
                    if where_r == "card":
                        card = random.choice(
                            list(self.game_rules.displayed_cards.values()))
                        self.game_rules.event(EventType.POPUP_RESERVE, card)
                        bool_action = True

            # Acheter
            if action_ia == "purchase":
                l_where_p = ["reserved", "visible"]
                where_p = random.choice(list(l_where_p))
                if l_where_p == "reserved":
                    l_card_r = self.reserved_cards
                    card_r = random.choice(self.reserved_cards)
                    for card_r in self.reserved_cards:
                        self.game_board.event(EventType.POPUP_PURCHASE, card_r)
                        break
                else:

                    count_card = 0
                    count_card_t = 0
                    l_lvl = [1, 2, 3]
                    while len(l_lvl) > 0:
                        l_lvl_r = random.choice(list(l_lvl))
                        for lvl in self.game_board.displayed_cards.keys():
                            if lvl == l_lvl_r:
                                for c in self.game_board.displayed_cards.values():
                                    if self.game_board.event(
                                            EventType.POPUP_PURCHASE, c):
                                        break
                                    else:
                                        count_card += 1
                                if count_card == 4:
                                    l_lvl.remove(l_lvl_r)
                                    count_card_t += 4
                                    count_card = 0
                        if count_card_t == self.game_board.nb_card_reveal:
                            l_action.remove(action_ia)
                            break

                # Rendre Token
                if self.game_board.game_state == \
                        self.game_state.PLAYER_GIVE_TOKENS_BACK:
                    while sum(self.bank.values()) > 10:
                        token_gb = random.choice(list(self.bank.items()))
                        self.game_rules.event(
                            EventType.CLICK_GIVE_BACK_PLAYER_TOKEN, token_gb)

                # Choisir Tile
                if self.game_board.game_state == \
                        self.game_state.PLAYER_CHOOSE_TILE:
                    for tiles_c in self.displayed_tiles:
                        self.game_rules.event(EventType.CLICK_TILE)

        # Pas sur
        if bool_action == False:
            self.game_board.end_turn()

    def action_AI_advanced(self):
        print("Hello IA")
        nb_turn = 0

    # Card Niveau 1 : Cout de gem = 3-5
    # Card Niveau 2 : Cout de gem = 5-8
    # Card Niveau 3 : Cout de gem =  7-14





    # def action_reserved_card(self):
