from copy import deepcopy

from src.element.Card import Card
from src.game.GameState import GameState
from src.player.Player import Player
from src.mvc.EventType import EventType
from src.mvc import GameBoard
from src.mvc import GameRules
import time
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
        print('AI - play')
        print("AI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.game_board.display.refresh()
        self.game_board.display.window.update()
        time.sleep(1)

        self.play_basic()
        #self.play_advanced()

    def play_basic(self):
        print('AI - basic')
        print("Fonction AI ???????????????????????????????????")
        self.l_action = ["purchase", "take", "reserved"]
        self.bool_action = False
        for i in range(0, len(self.l_action)):
            action_ia = random.choice(list(self.l_action))

            if action_ia == "take":
                self.take_gem()

            elif action_ia == "reserved":
                self.reserved()

            elif action_ia == "purchase":
                self.purchase()

            if self.bool_action:
                break

        givetoken = self.game_board.game_state == \
                    GameState.PLAYER_GIVE_TOKENS_BACK
        choosetile = self.game_board.game_state == \
                     GameState.PLAYER_CHOOSE_TILE

        print("AI Ending ???????????????????????????????????")
        self.ending_event(givetoken, choosetile)
        print("AI EVENT  ???????????????????????????????????")

    def take_gem(self):
        print('AI - take_gem')
        print("take Token")
        self.l_action.remove("take")
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

    def take_two(self, gem):
        print('AI - take_two')
        if self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                 gem):
            if self.game_rules.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                                     gem):
                self.bool_action = True

    def take_three(self):
        print('AI - take_three')
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
        print('AI - reserved')
        print("Reserv une carte")
        self.l_action.remove("reserved")
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

    def purchase(self):
        print('AI - purchase')
        # Acheter
        print("Acheter une carte")
        self.l_action.remove("purchase")
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

    def purchase_reserved(self, l_where_p):
        print('AI - purchase_reserved')
        l_where_p.remove("reserved")
        for card_r in self.reserved_cards:
                if card_r.is_purchasable(self.game_board.get_current_player()
                                .get_income()):
                    self.game_rules.event(EventType.RESERVE_PURCHASE,
                                     card_r)
                    self.bool_action = True
                    return

    def purchase_visible(self, l_where_p):
        print('AI - purchase_visible')
        l_where_p.remove("visible")
        for lvl in self.game_board.displayed_cards:
            for card in self.game_board.displayed_cards[lvl]:
                if card.is_purchasable(self.game_board.get_current_player()
                                .get_income()):
                    self.game_rules.event(EventType.POPUP_PURCHASE,
                                         card)
                    self.bool_action = True
                    return

    def ending_event(self, givetoken, choosetile):
        print('AI - ending_event')
        # Rendre Token
        if givetoken:
            print("Rendre "
                  "l'argent!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            while sum(self.bank.values()) > 10:
                token_gb = random.choice(list(self.bank.keys()))
                self.game_rules.event(
                    EventType.CLICK_GIVE_BACK_PLAYER_TOKEN, token_gb)

        # Choisir Tile
        if choosetile:
            print("Choisir une tile")
            for tiles_c in self.game_board.tiles:
                self.game_rules.event(EventType.CLICK_TILE, tiles_c)

    def play_advanced(self):
        print("Hello IA")
        self.bool_action = False
        l_card_purchase = self.find_efficientCard()
        print(l_card_purchase)
        if self.purchase_adv(l_card_purchase):
            bool_action = True

        l_gem = list()
        if not self.bool_action:
            l_gem = self.tokens_to_take()
            if self.take_adv(l_gem):
                self.bool_action = True
            elif self.reserved_card_adv():
                self.bool_action = True

        givetoken = self.game_board.game_state == \
                    GameState.PLAYER_GIVE_TOKENS_BACK
        choosetile = self.game_board.game_state == \
                     GameState.PLAYER_CHOOSE_TILE

        self.ending_event_adv(givetoken, choosetile)

        if not self.bool_action:
            self.game_board.end_action()



    def purchase_adv(self,l_card):
        for card in l_card:
            if card.is_purchasable(self.game_board.get_current_player()
                                    .get_income()):
                self.game_rules.event(EventType.POPUP_PURCHASE,
                                             card)
                return True
        return False


    def ending_event_adv(self, givetoken, choosetile):
        # Rendre Token
        if givetoken:

            print("Rendre "
                  "l'argent!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if sum(self.bank.values()) > 10:
                l_gem = self.tokens_to_take()
                for gem,val in self.bank:
                    if not gem in l_gem:
                        if val > 0:
                            self.game_rules.event(
                                EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                                gem)

                #Si il reste des tokens a rendre (alea)
                n = self.bank.values() - self.game_rules.nb_min_gem_stack
                if n > 0:
                    #Creation d'une copy des token de l'AI sans les piles à 0
                    d_bank = deepcopy(self.bank)
                    for k,v in d_bank:
                        if v == 0:
                            d_bank.remove(k)

                    for i in range (0,n):
                        type_gem = random.choice(list(d_bank))
                        self.game_rules.event(
                            EventType.CLICK_GIVE_BACK_PLAYER_TOKEN, type_gem)


        # Choisir Tile
        if choosetile:
            print("Choisir une tile")
            for tiles_c in self.game_board.displayed_tiles:
                self.game_rules.event(EventType.CLICK_TILE,tiles_c)


    def reserved_card_adv(self):
        print("Reserved_Advanced")
        l_card = self.find_efficientCard()
        card_r = random.choice(list(l_card))
        if len(self.reserved_cards) < self.game_rules.nb_max_res_card:
            if self.game_rules.event(EventType.POPUP_RESERVE, card_r):
                return True

            l_lvl= [1,2,3]
            for lvl in l_lvl:
                if self.game_rules.event(EventType.CLICK_DECK_CARD, lvl):
                    return True

            for lvl in l_lvl:
                for l_c in self.game_board.displayed_cards[lvl]:
                    for c in l_c:
                        if self.game_rules.event(EventType.POPUP_RESERVE, c):
                            return True
        return False


    def take_adv(self,gems):
        print("take Token")
        list_gem_dispo = list()
        for key in self.game_board.bank:
            if self.game_board.bank[key] > 0 and key != "Gold":
                list_gem_dispo.append(key)

        print("list_gem_dispo", list_gem_dispo)
        print("nb min gem stack", self.game_rules.nb_min_gem_stack)
        if len(list_gem_dispo) == 1 and self.game_board.bank[
            list_gem_dispo[0]] > self.game_rules.nb_min_gem_stack:
            self.game_rules.event(
                EventType.CLICK_TAKE_TOKEN_GAMEBOARD, list_gem_dispo[0])
            self.game_rules.event(
                EventType.CLICK_TAKE_TOKEN_GAMEBOARD, list_gem_dispo[0])
            return True

        elif len(list_gem_dispo) > 0:
            count = 0
            print(gems)
            for i in range(0, len(gems)-1):
                print("gems[i]", gems[i])
                if self.game_rules.event(
                    EventType.CLICK_TAKE_TOKEN_GAMEBOARD, gems[i]):
                    gems.remove(gems[i])

            if len(gems) > 0:
                for i in range (0, len(gems)):
                    for j in range (0, len(list_gem_dispo)):
                        if gems[i] == list_gem_dispo[j]:
                            self.game_rules.event(
                            EventType.CLICK_TAKE_TOKEN_GAMEBOARD, gems[i])
                            gems.remove(gems[i])
                            list_gem_dispo.remove(gems[i])
            else :
                return True

            if len(list_gem_dispo) > 0:
                if len(gems) > len(list_gem_dispo):
                    for i in range (0,len(list_gem_dispo)):
                        gem = random.choice(list(list_gem_dispo))
                        self.game_rules.event(
                            EventType.CLICK_TAKE_TOKEN_GAMEBOARD, gem)
                        list_gem_dispo.remove(gem)
                return True
        else:
            return False




    # Calcul de jeton manquant pour une carte
    def real_value_card(self, card):
        comp_dict = {}
        dict_inc = self.get_card_income()
        for key_card in card.purchase_gems:
            for key_inc in dict_inc:
                if key_card == key_inc:
                    comp_dict = card.purchase_gems[key_card] - \
                                dict_inc[key_inc]
        return comp_dict

    #return number of turn of card
    def worth_it(self, card):
        print("WORTH IT")
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


    # Return: Dictionnary of tokens ratio
    def tokens_to_take(self):
        print("TOKENS TO TAKE")

        l_card = self.find_efficientCard()
        #for c in l_c:
            #l_card.append(self.real_value_card(c))

        dict_nb_gem = {}
        dict_nb_type = {}
        dict_gem_type = {}
        ratio = dict()

        # Initialize the gems dictionnary
        for card in l_card:
            for type_gem, val_gem in card.purchase_gems.items():
                dict_nb_gem[type_gem] = 0

        # Pour chaque carte on ajoute la valeur du gem correspondant dans le dictionnaire
        for card in l_card:
            for type_gem, val_gem in card.purchase_gems.items():
                dict_nb_gem[type_gem] += val_gem

        # Initialize the type dictionnary
        for card in l_card:
            for type_gem, val_gem in card.purchase_gems.items():
                dict_nb_type[type_gem] = 0

        # Pour chaque carte on ajoute +1 au type de gem présent dans la carte
        for card in l_card:
            for type_gem, val_gem in card.purchase_gems.items():
                if val_gem != 0:
                    dict_nb_type[type_gem] += 1

        # Initialize the gems dictionnary
        for card in l_card:
            for type_gem, val_gem in card.purchase_gems.items():
                dict_gem_type[type_gem] = 0

        # Comparer les deux dictionnaires et mettre le ratio dans le nouveau
        for type_gem, val_gem in dict_nb_type.items():
            if dict_nb_gem[type_gem] != 0:
                if type_gem in dict_nb_gem:
                    ratio[type_gem] = val_gem / dict_nb_gem[type_gem]
                else:
                    ratio[type_gem] = val_gem
        print(ratio, " : ratio de retour")

        #Trouver la liste de gem a take
        dict_tokens_to_take = deepcopy(ratio)
        print("DICT TOKEN TO TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKE")
        print(dict_tokens_to_take)
        l_gem = list()
        l_type_see = list()
        for i in range(1,4):
            #ratio_max = max(dict_tokens_to_take.iteritems(), key=ratio.get)
            max_gem = 0
            max_type = None
            for key,val in dict_tokens_to_take.items():
                if max_gem < val:
                    print("ok1")
                    max_type = key
                    max_gem = val
                    print(max_type)
            if max_gem != 0:
                print("ok2")
                l_gem.append(max_type)
                del dict_tokens_to_take[max_type]
        print(l_gem)
        return l_gem


    # Return: Dictionnary of most efficient card
    def find_efficientCard(self):
        print("FIN EFFICIENT CARD")
        card_efficient = []
        dict_card = deepcopy(self.game_board.displayed_cards)

        if self.purchased_card_amount < 6:

            # Remplir une liste carte lvl 1
            l_card_1 = []
            for k, l_card in dict_card.items():
                if k == 1:
                    l_card_1 = l_card

            print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
            print(l_card_1)
            # Dictionnaire : clé le nombre de tour et la valeur une liste de
            # carte
            dict_turn = {}
            n = 0
            for card in l_card_1:
                n = self.worth_it(card)
                dict_turn[n] = card
        while(len(card_efficient) != len(dict_turn)):
            top_effi = max(dict_turn, key=dict_turn.get)
            card_efficient.append(dict_turn[top_effi])

        if self.purchased_card_amount >= 6:
            print("yolo")
        return card_efficient

    #def action_ai_advanced(self):





