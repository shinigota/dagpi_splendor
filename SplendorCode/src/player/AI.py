from src.player.Player import Player
from src.mvc.EventType import EventType
from src.mvc import GameBoard
from src.mvc import GameRules
import random

class AI(Player):
    difficulty = None

    def __init__(self, name, position, difficulty):
        Player.__init__(self, name, position)
        self.dificulty = difficulty

    def basic_mod(self, ):
        dict = {}
        random.choice(list(dict.keys()))


    def action_AI(self):
        l_action = ["two","tree","reserved","purchase"]
        while(len(l_action)>1):
            nb = random.choice(list(l_action))
            if nb == "two":
                l_type_t2 = []
                while (len(l_type_t2) == 0):
                    (token_type_t2,token_nb_t2) = random.choice(list(GameBoard.bank.items()))
                    if token_nb_t2 >= 2 and token_type_t2 not in l_type_t2:
                        #token = recuperer dans GameBoard
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)
                        l_type_t2.append(token_type_t2)

            if nb == "tree":
                l_type_t3 = []
                while (len(l_type_t3) < 3):
                    (token_type_t3,token_nb_t3) = random.choice(list(GameBoard.bank.items()))
                    if token_nb_t3 >= 1 and token_type_t3 not in l_type_t3:
                        l_type_t3.append(token_type_t3)
                        #token = recuperer dans GameBoard
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)

            if nb == "reserved":
                if self.reserved_cards == 3:
                    l.remove["reserved"]
                where = random.choice("deck","visible")
                l_lvl = [1,2,3]
                if where == "deck":
                    EventType.event(EventType.CLICK_DECK_CARD, random.choice(list(l_lvl)))
                if where == "card":
                    #card = recuperer la carte dans GameBoard
                    EventType.event(EventType.POPUP_RESERVE, card)

            if nb == "purchase":
                while(True):
                    if self.reserved_cards == GameRules.nb_max_res_card:
                        break
                    l_lvl = [1, 2, 3]
                    l_lvl_card = random.choice(list(l_lvl))
                    #card = recuperer la carte dans GameBoard
                    EventType.event(EventType.POPUP_PURCHASE, card)
                    break

        #passez le tour







    #def action_reserved_card(self):


