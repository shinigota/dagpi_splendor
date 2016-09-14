from src.player.Player import Player
from src.mvc.EventType import EventType
from src.mvc import GameBoard
from src.mvc import GameRules
import random

class AI(Player):
    difficulty = None

    def __init__(self, position, difficulty, gb, gr, ci, pi):
        Player.__init__()
        self.dificulty = difficulty
        self.position = position

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
                    (token_type_t2, token_nb_t2) = random.choice(list(GameBoard.bank.items()))
                    if token_nb_t2 >= 2 and token_type_t2 not in l_type_t2:
                        #token = recuperer dans GameBoard
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)
                        l_type_t2.append(token_type_t2)

            if nb == "three":
                l_type_t3 = []
                while (len(l_type_t3) < 3):
                    (token_type_t3,token_nb_t3) = random.choice(list(GameBoard.bank.items()))
                    if token_nb_t3 >= 1 and token_type_t3 not in l_type_t3:
                        l_type_t3.append(token_type_t3)
                        #token = recuperer dans GameBoard
                        EventType.event(EventType.CLICK_TAKE_TOKEN_GAMEBOARD, token)

            if nb == "reserved":
                if self.reserved_cards == 3:
                    l.action.remove["reserved"]
                where = random.choice("deck", "visible")
                l_lvl = [1,2,3]
                if where == "deck":
                    EventType.event(EventType.CLICK_DECK_CARD, random.choice(list(l_lvl)))
                if where == "card":
                    #card = recuperer la carte dans GameBoard
                    EventType.event(EventType.POPUP_RESERVE, card)

            if nb == "purchase":
                while(True):
                    for lvl in GameBoard.displayed_cards.keys():
                        for card in GameBoard.displayed_cards.values():
                            GameRules.event(EventType.POPUP_PURCHASE, card)
                        else:
                            break

                    #card = recuperer la carte dans GameBoard

                    break

        #passez le tour




    def find_efficientCard(self):
        for
        self.cards_info = list(self)

        while Player.purchased_card_amount < 6:
            for card in self.GameBoard.displayed_cards[card.get_level() == 1]:
                #             if card.get_level() == 1:
                self.cards_info[card] = card.purchase_gems()
 #               print(self.cards_info[card])
            for card in self.cards_info:
                self.card_info[card] = AI.worth_it(card)









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






















                #def action_reserved_card(self):


