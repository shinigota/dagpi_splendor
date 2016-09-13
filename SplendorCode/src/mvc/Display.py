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

    def display_tiles(self):
        i = 1
        for tile in self.game_board.displayed_tiles:
            self.display_tile(i, tile)
            i += 1

    def display_tile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100,
                        background='#725202')
        points = canvas.create_text(10, 10, text=tile.points, fill="black")
        i = 1
        for key in tile.gems_conditions:
            number = tile.gems_conditions[key]
            if number > 0:
                textcolor = "white"
                if RessourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    cardBuy1 = canvas.create_rectangle(10, 25, 40, 55,
                                                       fill=RessourceType.get_color(
                                                           key))
                    txtBuy1 = canvas.create_text(25, 40, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    cardBuy2 = canvas.create_rectangle(10, 65, 40, 95,
                                                       fill=RessourceType.get_color(
                                                           key))
                    txtBuy2 = canvas.create_text(25, 80, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    cardBuy3 = canvas.create_rectangle(60, 65, 90, 95,
                                                       fill=RessourceType.get_color(
                                                           key))
                    txtBuy3 = canvas.create_text(75, 80, text=number,
                                                 fill=textcolor)
                    i = 0
        canvas.place(x=170 + 120 * (position - 1), y=100)
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_TILE,
                                         t=tile: self.game_rules.event(e, t))

    def display_cards(self):
        for lvl in range(1, int(self.game_rules.nb_lvl_card) + 1):
            i = 1
            for card in self.game_board.displayed_cards[lvl]:
                x = 170 + 120 * (i - 1)
                y = 490 - (130 * (lvl - 1))
                self.display_card(self.window, x, y, card)
                i += 1

    def display_card(self, canvas, x, y, card):
        canvas = Canvas(self.window, width=100, height=120,
                        background=self.get_color(int(card.level)))
        points = canvas.create_text(10, 10, text=card.points, fill="black")

        gem = canvas.create_oval(85, 5, 95, 15,
                                 fill=RessourceType.get_color(
                                     card.income_gem))
        i = 1
        for key in card.purchase_gems:
            number = card.purchase_gems[key]
            if number > 0:
                textcolor = "white"
                if RessourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    gemBuy1 = canvas.create_oval(10, 85, 40, 115,
                                                 fill=RessourceType.get_color(
                                                     key))
                    txtBuy1 = canvas.create_text(25, 100, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    gemBuy2 = canvas.create_oval(60, 85, 90, 115,
                                                 fill=RessourceType.get_color(
                                                     key))
                    txtBuy2 = canvas.create_text(75, 100, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    gemBuy3 = canvas.create_oval(10, 45, 40, 75,
                                                 fill=RessourceType.get_color(
                                                     key))
                    txtBuy3 = canvas.create_text(25, 60, text=number,
                                                 fill=textcolor)
                    i = 4
                elif i == 4:
                    gemBuy4 = canvas.create_oval(60, 45, 90, 75,
                                                 fill=RessourceType.get_color(
                                                     key))
                    txtBuy4 = canvas.create_text(75, 60, text=number,
                                                 fill=textcolor)
                    i = 0
        canvas.place(x=x,
                     y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_DISPLAYED_CARD,
                           c=card: self.game_rules.event(e, c))

    def display_piles(self):
        self.display_pile(1, False)
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
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

    def display_bank(self, bank):
        x = 70
        y = 650
        for token in bank.keys():
            if token == "Gold":
                self.display_gold(self.window, 70, 115, bank[token])
            else:
                self.display_gem(self.window, x, y, bank[token], token)
                x += 100

    def display_gold(self, canvas, x, y, nb):
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=RessourceType.get_color("Gold"))
        canvas.create_text(40, 40, text=nb, fill="black")
        canvas.place(x=x, y=y)

    def display_gem(self, canvas, x, y, nb, gem):
        color = "white"
        if RessourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=RessourceType.get_color(gem))
        canvas.create_text(40, 40, text=nb, fill=color)
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                           g=gem: self.game_rules.event(e, g))

    def display_player_bank(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=100, height=100)
        x = 10
        y = 10
        for token in player.bank.keys():
            if token == "Gold":
                self.display_player_gold(canvas, 50, 50, player.bank[token])
            else:
                self.display_player_gem(canvas, x, y, player.bank[token],
                                        token)
                x += 60
        canvas.place(x=x, y=y)

    def display_player_gem(self, canvas, x, y, nb, gem):
        color = "white"
        if RessourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_oval(10, 10, 50, 50,
                           fill=RessourceType.get_color(gem))
        canvas.create_text(20, 20, text=nb, fill=color)
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                           g=gem: self.game_rules.event(e, g))

    def display_player_gold(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=60, height=60)
        canvas.place(x=x, y=y)

    def display_player_income_card(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=80, height=80)
        canvas.place(x=x, y=y)

    @staticmethod
    def get_color(level):
        if level == 1:
            color = '#0483f9'
        if level == 2:
            color = '#05e002'
        if level == 3:
            color = '#ffac07'
        return color

    def refresh(self):

        self.display_bank(self.game_board.bank)
        self.display_piles()
        self.display_cards()
        self.display_tiles()
        self.display_player_bank(self.window, 100, 100, self.game_board.get_current_player())


display = Display()
display.game_board = GameBoard(display, GameRules())
display.game_rules = display.game_board.game_rules
display.game_rules.game_board = display.game_board
display.create_window()
display.refresh()
display.window.mainloop()
