from copy import deepcopy

from src.element.Card import Card
from src.game.GameState import GameState
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

    def play(self):
        print("AI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.play_basic()

    def play_basic(self):
        print("Fonction AI ???????????????????????????????????")
        self.l_action = ["take", "purchase", "reserved"]
        self.bool_action = False
        action_ia = None
        while len(self.l_action) > 0 and not self.bool_action:
            action_ia = random.choice(list(self.l_action))

            if action_ia == "take":
                self.take_gem()

            elif action_ia == "reserved":
                self.reserved()

            elif action_ia == "purchase":
                self.purchase()

        givetoken = self.game_board.game_state == \
                    GameState.PLAYER_GIVE_TOKENS_BACK
        choosetile = self.game_board.game_state == \
                     GameState.PLAYER_CHOOSE_TILE

        print("AI Ending ???????????????????????????????????")
        self.ending_event(givetoken, choosetile)
        print("AI EVENT  ???????????????????????????????????")
        if not self.bool_action:
            print("AI NO ACTION ???????????????????????????????????")
            self.game_board.end_action()

    def take_gem(self):
        print("take Token")
        list_gem = list()
        list_choice = list()
        list_choice.append("two")
        list_choice.append("three")
        take = random.choice(list_choice)
        if take == "two":
            print("take two")
            for key in self.game_board.bank:
                if self.game_board.bank[key] >= \
                        self.game_rules.nb_min_gem_stack and key != "Gold":
                    list_gem.append(key)
            print(list_gem)
            if len(list_gem) > 0:
                gem = random.choice(list_gem)
                self.take_two(gem)
            else:
                print("take three")
                self.take_three()
        else:
            print("take three")
            self.take_three()
        self.l_action.remove("take")

    def take_two(self, gem):
        if self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                 gem):
            if self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                     gem):
                self.bool_action = True

    def take_three(self):
        list_gem = list()
        for key in self.game_board.bank:
            if self.game_board.bank[key] > 0 and key != "Gold":
                list_gem.append(key)
        if len(list_gem) > 0:
            print("Bouclu")
            print(self.game_rules.nb_gem_diff)
            for i in range(0, self.game_rules.nb_gem_diff):
                print(i)
                if len(list_gem) > 0:
                    gem = random.choice(list_gem)
                    self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                          gem)
                    list_gem.remove(gem)
            self.bool_action = True

    def reserved(self):
        print("Reserv une carte")
        if len(self.reserved_cards) < self.game_rules.nb_max_res_card:
            l_where_r = ["deck", "card"]
            where_r = random.choice(list(l_where_r))
            l_lvl = [1, 2, 3]
            if where_r == "deck":
                print('LEVEL')
                print(l_lvl)
                lvl = random.choice(list(l_lvl))
                if not self.game_board.is_deck_empty(lvl):
                    self.game_rules.event(EventType.CLICK_DECK_CARD,
                                          lvl)
                    self.bool_action = True
            elif where_r == "card":
                for i in range(0, self.game_rules.nb_lvl_card):
                    lvl = random.choice(list(l_lvl))
                    if len(self.game_board.displayed_cards[lvl]) > 0:
                        card = random.choice(
                            list(self.game_board.displayed_cards[lvl]))
                        print('CARD')
                        print(card)
                        self.game_rules.event(EventType.POPUP_RESERVE, card)
                        self.bool_action = True
                        break
                    l_lvl.remove(lvl)
        self.l_action.remove("reserved")

    def purchase(self):
        # Acheter
        print("Acheter une carte")
        l_where_p = ["reserved", "visible"]
        where_p = None
        if len(self.reserved_cards) > 1:
            where_p = random.choice(list(l_where_p))
            if where_p == "reserved":
                self.purchase_reserved(l_where_p)
                if not self.bool_action:
                    self.purchase_visible(l_where_p)
            else:
                self.purchase_visible(l_where_p)
                if not self.bool_action:
                    self.purchase_reserved(l_where_p)
        else:
            self.purchase_visible(l_where_p)
        self.l_action.remove("purchase")

    def purchase_reserved(self, l_where_p):
        for card_r in self.reserved_cards:
            if self.game_rules.event(EventType.POPUP_PURCHASE,
                                     card_r):
                bool_action = True
                break
        l_where_p.remove("reserved")

    def purchase_visible(self, l_where_p):
        for lvl in self.game_board.displayed_cards:
            for card in self.game_board.displayed_cards[lvl]:
                if self.game_rules.event(EventType.POPUP_PURCHASE,
                                         card):
                    bool_action = True
                    break
        l_where_p.remove("visible")

    def ending_event(self, givetoken, choosetile):
        # Rendre Token
        if givetoken:

            print("Rendre "
                  "l'argent!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            while sum(self.bank.values()) > 10:
                token_gb = random.choice(list(self.bank.items()))
                self.game_rules.event(
                    EventType.CLICK_GIVE_BACK_PLAYER_TOKEN, token_gb)

        # Choisir Tile
        if choosetile:
            print("Choisir une tile")
            for tiles_c in self.displayed_tiles:
                self.game_rules.event(EventType.CLICK_TILE)

    def action_AI_advanced(self):
        print("Hello IA")
        nb_turn = 0

    # Calcul de jeton manquant pour une carte
    def real_value_card(self, card):
        comp_dict = {}
        dict_inc = self.get_card_income()
        for key_card in card.items():
            for key_inc in dict_inc:
                if key_card == key_inc:
                    comp_dict = card.values() - dict_inc.values()
        return comp_dict

    def worth_it(card):
        print(card.__dict__)
        count_turn = 0
        card_comp = None
        card_comp = deepcopy(card)
        bool_count = False
        while not bool_count:
            print("debut", count_turn)
            print("debut", bool_count)
            count_type = 0

            for type_card, val_card in card_comp.purchase_gems.items():
                if val_card > 0:
                    count_type += 1
            print("Count_type", count_type)
            if count_type >= 2:
                count_ite = 0
                max_gem = max(card_comp.purchase_gems,
                              key=card_comp.purchase_gems.get)
                for type_card, val_card in card_comp.purchase_gems.items():
                    if val_card > 0:
                        print("Cycle_d", card_comp.purchase_gems[type_card])
                        card_comp.purchase_gems[type_card] -= 1
                        print("Cycle_f", card_comp.purchase_gems[type_card])
                        count_ite += 1
                    if count_ite == 3:
                        count_turn += 1
                        break
                    if count_type == 2 and count_ite == 2:
                        count_turn += 1
                        break
            elif count_type == 1:
                for type_card, val_card in card_comp.purchase_gems.items():
                    if val_card >= 2:
                        card_comp.purchase_gems[type_card] -= 2
                        count_turn += 1
                    elif val_card == 1:
                        card_comp.purchase_gems[type_card] -= 1
                        count_turn += 1
            elif count_type == 0:
                print("FIN")
                print(card_comp.__dict__)
                bool_count = True
        return count_turn

    # Card Niveau 1 : Cout de gem = 3-5
    # Card Niveau 2 : Cout de gem = 5-8
    # Card Niveau 3 : Cout de gem =  7-14


    def find_efficientCard(self):
        card_efficient = []
        dict_card = deepcopy(self.game_board.displayed_cards)

        if self.purchased_card_amount < 6:

            # Remplir une liste carte lvl 1
            l_card_1 = []
            for k, l_card in dict_card.items():
                if k == 1:
                    l_card_1 = l_card

            # Dictionnaire : clé le nombre de tour et la valeur une liste de
            # carte
            dict_turn = (list)
            n = 0
            for card in l_card_1:
                n = self.worth_it(card)
                dict_turn[n].append(card)

            top_effi = min(dict, key=dict.get)
            card_efficient = dict_turn[top_effi]

        if self.purchased_card_amount >= 6:
            print("yolo")

        return card_efficient

    def action_ai_advanced(self):

        l_card = []
        l_card = self.find_efficientCard()
        dict_nb_gem = {}

        for c in l_card:
            for type_gem, val_gem in c.purchase_gems.items():
                dict_nb_gem[type_gem] += val_gem


dict_c_cost = {}
dict_c_cost["Emerald"] = 3
dict_c_cost["Saphir"] = 2
dict_c_cost["Ruby"] = 1

dict_c_cost1 = {}
dict_c_cost1["Emerald"] = 1
dict_c_cost1["Saphir"] = 2
dict_c_cost1["Ruby"] = 3

dict_nb_gem = {}

for type_gem in dict_c_cost.keys():
    dict_nb_gem[type_gem] = 0

for type_gem, val_gem in dict_c_cost.items():
    print("type_gem", type_gem)
    print("val_gem", val_gem)
    dict_nb_gem[type_gem] += val_gem
    print(dict_nb_gem)

print(dict_nb_gem)

'''
mostEfficientCards = dict()
min_turn = 99

for card in self.cards_info:
    if card_info[card].values() == min_turn:
        mostEfficientCards[card]'''




#
# the_card = self.cards_info[card]
# card_min = None
# for card in self.cards_info:
#     min_values  =   min(the_card)
#
#






















# def action_reserved_card(self):
