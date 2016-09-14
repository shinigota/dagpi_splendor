from copy import deepcopy

from src.element.Card import Card
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

    def __init__(self, name, position, difficulty):
        Player.__init__(self, name, position)
        self.dificulty = difficulty
        self.position = position


    def action_AI_basic(self):

        l_action = ["two", "three", "reserved", "purchase"]
        bool_action = False

        while len(l_action) > 1 or not bool_action:
            action_ia = random.choice(list(l_action))

            if action_ia == "two":
                dict_t2 = {}
                for k, v in GameBoard.bank.items():
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
                            EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token_t3)
                        del dict_t3[token_type_t3]
                    bool_action = True

            if action_ia == "reserved":
                while not bool_action:
                    if self.reserved_cards == self.game_rules.nb_max_res_card:
                        l_action.remove(action_ia)
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

            #Acheter
            if action_ia == "purchase":
                l_where_p = ["reserved", "visible"]
                where_p = random.choice(list(l_where_p))
                if l_where_p == "reserved":
                    l_card_r = self.reserved_cards
                    card_r = random.choice(self.reserved_cards)
                    for card_r in self.reserved_cards:
                        self.game_board.event(EventType.POPUP_PURCHASE, card_r)
                        break
                else :

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

                #Rendre Token
                if self.game_board.game_state == \
                        self.game_state.PLAYER_GIVE_TOKENS_BACK:
                    while sum(self.bank.values()) > 10:
                        token_gb = random.choice(list(self.bank.items()))
                        self.game_rules.event(
                            EventType.CLICK_GIVE_BACK_PLAYER_TOKEN, token_gb)

                #Choisir Tile
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


#Calcul de jeton manquant pour une carte
def real_value_card(self,card):
    comp_dict = {}
    dict_inc = self.get_card_income()
    for key_card in card.items():
        for key_inc in dict_inc:
            if key_card == key_inc:
                comp_dict = card.values() - dict_inc.values()
    return comp_dict


def worth_it (card):
    print(card.__dict__)
    count_turn = 0
    card_comp = None
    card_comp = deepcopy(card)
    bool_count = False
    while not bool_count:
        print("debut",count_turn)
        print("debut",bool_count)
        count_type = 0

        for type_card, val_card in card_comp.purchase_gems.items():
            if val_card > 0:
                count_type += 1
        print("Count_type",count_type)
        if count_type >= 2:
            count_ite = 0
            for type_card, val_card in card_comp.purchase_gems.items():
                if val_card > 0:
                    print("Cycle_d", card_comp.purchase_gems[type_card])
                    card_comp.purchase_gems[type_card] -= 1
                    print("Cycle_f", card_comp.purchase_gems[type_card])
                    count_ite +=1
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







c = Card(3, "Saphir", {'Saphir': 1, 'Ruby': 1, 'Onyx': 1, 'Diamond': 1,
                       'Emerald': 0}, 1)
n = worth_it(c)
print(n)






#Card Niveau 1 : Cout de gem = 3-5
#Card Niveau 2 : Cout de gem = 5-8
#Card Niveau 3 : Cout de gem =  7-14





        # def action_reserved_card(self):


