from tkinter import *

from src.element.Card import Card
from src.element.RessourceType import RessourceType
from src.mvc.EventType import EventType
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Display:
    window = None
    text = "test"
    game_rules = None
    game_board = None
    w = None
    h = None

    def __init__(self):
        self.window = Tk()

    def create_window(self):
        self.window.title(GameRules.game_name)
        self.w, self.h = 1900, 1000
        self.window.overrideredirect(0)
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))

    def display_tile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100,
                        background='#725202')
        points = canvas.create_text(10, 10, text=0, fill="black")
        cardBuy1 = canvas.create_rectangle(10, 25, 40, 55, fill="red")
        cardBuy2 = canvas.create_rectangle(10, 65, 40, 95, fill="blue")
        cardBuy3 = canvas.create_rectangle(60, 65, 90, 95, fill="green")
        txtBuy1 = canvas.create_text(25, 40, text="0", fill="white")
        txtBuy2 = canvas.create_text(25, 80, text="0", fill="white")
        txtBuy3 = canvas.create_text(75, 80, text="0", fill="white")
        canvas.place(x=170 + 120 * (position - 1), y=100)
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_TILE,
                                         t=tile: self.game_rules.event(e, t))

    def display_cards(self):
        for lvl in range(1, int(self.game_rules.nb_lvl_card) + 1):
            i = 1
            for card in self.game_board.displayed_cards[lvl]:
                x = 170 + 120 * (i - 1)
                y = 490 - (130 * (lvl - 1))
                self.display_card(x, y, card)
                i += 1

    def display_card(self, x, y, card):
        canvas = Canvas(self.window, width=100, height=120,
                        background=self.get_color(card.level))
        points = canvas.create_text(10, 10, text=0, fill="black")
        gem = canvas.create_oval(85, 5, 95, 15,
                                 fill=RessourceType.get_ressource_color(
                                     card.income_gem))
        gemBuy1 = canvas.create_oval(10, 85, 40, 115,
                                     fill=RessourceType.get_ressource_color(
                                         card.income_gem))
        gemBuy2 = canvas.create_oval(60, 85, 90, 115,
                                     fill=RessourceType.get_ressource_color(
                                         card.income_gem))
        gemBuy3 = canvas.create_oval(10, 45, 40, 75,
                                     fill=RessourceType.get_ressource_color(
                                         card.income_gem))
        gemBuy4 = canvas.create_oval(60, 45, 90, 75,
                                     fill=RessourceType.get_ressource_color(
                                         card.income_gem))
        textcolor = "white"
        if RessourceType.get_ressource_color(card.income_gem) == "white":
            textcolor = "black"
        txtBuy1 = canvas.create_text(25, 100, text=0, fill=textcolor)
        txtBuy2 = canvas.create_text(75, 100, text=0, fill=textcolor)
        txtBuy3 = canvas.create_text(25, 60, text=0, fill=textcolor)
        txtBuy4 = canvas.create_text(75, 60, text=0, fill=textcolor)
        canvas.place(x=x,
                     y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_DISPLAYED_CARD,
                           c=card: self.game_rules.event(e, c))

    def display_piles(self):
        self.display_pile(1, False)
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            print(i)
            self.display_pile(i, self.game_board.is_deck_empty(i))

    def display_pile(self, level, empty):
        color = Display.get_color(level)
        if empty:
            color = "grey"
        canvas = Canvas(self.window, width=100, height=120, background=color)
        canvas.create_text(50, 50, text="PILE DE NIVEAU", fill="black")
        canvas.create_text(50, 70, text=level, fill="black")
        canvas.place(x=50, y=490 - (130 * (level - 1)))
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_DECK_CARD,
                                         l=level: self.game_rules.event(e, l))

    def display_gold(self, nb):
        canvas = Canvas(self.window, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=RessourceType.get_ressource_color("Gold"))
        canvas.create_text(40, 40, text=nb, fill="black")
        canvas.place(x=70, y=115)

    def display_gem(self, nb, gem):
        color = "white"
        if RessourceType.get_ressource_color(gem) == "white":
            color = "black"
        canvas = Canvas(self.window, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=RessourceType.get_ressource_color(gem))
        canvas.create_text(40, 40, text=nb, fill=color)
        canvas.place(x=Display.get_place(gem), y=650)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                           g=gem: self.game_rules.event(e, g))

    @staticmethod
    def get_color(level):
        if level == 1:
            color = '#0483f9'
        if level == 2:
            color = '#05e002'
        if level == 3:
            color = '#ffac07'
        return color

    @staticmethod
    def get_place(gem_name):
        if gem_name == "Diamond":
            place = 70
        if gem_name == "Ruby":
            place = 150
        if gem_name == "Onyx":
            place = 230
        if gem_name == "Emerald":
            place = 310
        if gem_name == "Sapphire":
            place = 390
        if gem_name == "Gold":
            place = 470
        return place

    def display_bank(self, bank):
        for token in bank.keys():
            if token == "Gold":
                self.display_gold(bank[token])
            else:
                self.display_gem(bank[token], token)

    def refresh(self):

        self.display_bank(self.game_board.bank)
        self.display_piles()
        self.display_cards()

        self.display_tile(1, None)
        self.display_tile(2, None)
        self.display_tile(3, None)
        self.display_tile(4, None)
        self.display_tile(5, None)


display = Display()
display.game_board = GameBoard(display, GameRules())
display.game_rules = display.game_board.game_rules
display.create_window()
display.refresh()
display.window.mainloop()
