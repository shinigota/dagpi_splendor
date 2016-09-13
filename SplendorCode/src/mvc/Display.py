from tkinter import *

from src.element.Card import Card
from src.element.ResourceType import ResourceType
from src.mvc.EventType import EventType
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules
from src.player.AI import AI


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
                if ResourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    cardBuy1 = canvas.create_rectangle(10, 25, 40, 55,
                                                       fill=ResourceType.get_color(
                                                           key))
                    txtBuy1 = canvas.create_text(25, 40, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    cardBuy2 = canvas.create_rectangle(10, 65, 40, 95,
                                                       fill=ResourceType.get_color(
                                                           key))
                    txtBuy2 = canvas.create_text(25, 80, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    cardBuy3 = canvas.create_rectangle(60, 65, 90, 95,
                                                       fill=ResourceType.get_color(
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
        canvas = Canvas(canvas, width=100, height=120,
                        background=self.get_color(int(card.level)))
        points = canvas.create_text(10, 10, text=card.points, fill="black")

        gem = canvas.create_oval(85, 5, 95, 15,
                                 fill=ResourceType.get_color(
                                     card.income_gem))
        i = 1
        for key in card.purchase_gems:
            number = card.purchase_gems[key]
            if number > 0:
                textcolor = "white"
                if ResourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    gemBuy1 = canvas.create_oval(10, 85, 40, 115,
                                                 fill=ResourceType.get_color(
                                                     key))
                    txtBuy1 = canvas.create_text(25, 100, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    gemBuy2 = canvas.create_oval(60, 85, 90, 115,
                                                 fill=ResourceType.get_color(
                                                     key))
                    txtBuy2 = canvas.create_text(75, 100, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    gemBuy3 = canvas.create_oval(10, 45, 40, 75,
                                                 fill=ResourceType.get_color(
                                                     key))
                    txtBuy3 = canvas.create_text(25, 60, text=number,
                                                 fill=textcolor)
                    i = 4
                elif i == 4:
                    gemBuy4 = canvas.create_oval(60, 45, 90, 75,
                                                 fill=ResourceType.get_color(
                                                     key))
                    txtBuy4 = canvas.create_text(75, 60, text=number,
                                                 fill=textcolor)
                    i = 0
        canvas.place(x=x,
                     y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_DISPLAYED_CARD,
                           c=card: self.game_rules.event(e, c))

    def display_stacks(self):
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            self.display_stack(i, self.game_board.is_deck_empty(i))

    def display_stack(self, level, empty):
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
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                self.display_gold(self.window, 70, 115, bank[token])
            else:
                self.display_gem(self.window, x, y, bank[token], token)
                x += 100

    def display_gold(self, canvas, x, y, nb):
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=ResourceType.get_color("Gold"))
        canvas.create_text(40, 40, text=nb, fill="black")
        canvas.place(x=x, y=y)

    def display_gem(self, canvas, x, y, nb, gem):
        color = "white"
        if ResourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70,
                           fill=ResourceType.get_color(gem))
        canvas.create_text(40, 40, text=nb, fill=color)
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                           g=gem: self.game_rules.event(e, g))

###################### Display hand of player #################################

    def display_players(self):
        x = 1300
        y = 40
        for player in self.game_board.players:
            if type(player) == AI:
                self.display_player_ia(x, y, player)
                y += 280
            else:
                self.display_player_human(player)

    def display_player_human(self,player):
        color = "grey"
        if self.game_board.get_current_player() == player:
            color = "orange"
        canvas = Canvas(self.window, width=500, height=270,
                        highlightbackground=color)
        self.display_player_bank(canvas, 100, 10, player)
        canvas.create_text(50, 45, text=player.nickname, fill="black")
        canvas.create_text(50, 65, text=str(player.calcul_point_in_game()) +
                                        " / "
                                        "" +
                                        self.game_rules.nb_points_end,
                           fill="black")
        y = 130
        i = 1
        for card in player.reserved_cards:
            x = 10 + 120 * (i - 1)
            self.display_card(canvas, x, y, card)
            i += 1
        self.display_player_tile(canvas, 370, 140, player)
        canvas.place(x=750, y=320)

    def display_player_ia(self, x, y,player):
        color = "grey"
        if self.game_board.get_current_player() == player:
            color = "orange"
        canvas = Canvas(self.window, width=500, height=270,
                        highlightbackground=color)
        canvas.place(x=x, y=y)
        self.display_player_bank(canvas, 100, 10, player)
        canvas.create_text(50, 45, text=player.nickname, fill="black")
        canvas.create_text(50, 65, text=str(player.calcul_point_in_game()) +
                                        " / "
                                        "" +
                                        self.game_rules.nb_points_end,
                           fill="black")
        y = 130
        i = 1
        for card in player.reserved_cards:
            x = 10 + 120 * (i - 1)
            self.display_card_ia(canvas, x, y, card.level)
            i += 1
        self.display_player_tile(canvas, 370, 140, player)

    def display_card_ia(self, canvas, x, y, level):
        color = Display.get_color(level)
        canvas = Canvas(canvas, width=100, height=120, background=color)
        canvas.place(x=x, y=y)

    def display_player_tile(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=100, height=100,
                        background='#725202')
        canvas.create_text(50, 50, text=len(player.owned_tiles), fill="black")
        canvas.place(x=x, y=y)

    def display_player_bank(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=390, height=120)
        canvas.place(x=x, y=y)
        x = 0
        y = 60
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                self.display_player_gold(canvas, 320, 30, player.bank[token])
            else:
                self.display_player_gem(canvas, x, y, player.bank[token],
                                        token)
                x += 60
        x = 0
        y = 0
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                pass
            else:
                self.display_player_income_card(canvas, x, y,
                                                player.get_card_income()[
                                                    token],
                                                token)
                x += 60

    def display_player_gold(self, canvas, x, y, nb):
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_oval(10, 10, 50, 50,
                           fill=ResourceType.get_color("Gold"))
        canvas.create_text(30, 30, text=nb, fill="black")
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                           g="Gold": self.game_rules.event(e, g))

    def display_player_gem(self, canvas, x, y, nb, gem):
        color = "white"
        if ResourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_oval(10, 10, 50, 50,
                           fill=ResourceType.get_color(gem))
        canvas.create_text(30, 30, text=nb, fill=color)
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                           g=gem: self.game_rules.event(e, g))

    def display_player_income_card(self, canvas, x, y, nb, gem):
        color = "white"
        if ResourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_rectangle(10, 10, 50, 50,
                                fill=ResourceType.get_color(gem))
        canvas.create_text(30, 30, text=nb, fill=color)
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
        self.display_stacks()
        self.display_cards()
        self.display_tiles()
        self.display_players()


display = Display()
display.game_board = GameBoard(display, GameRules())
display.game_rules = display.game_board.game_rules
display.game_rules.game_board = display.game_board
display.create_window()
display.refresh()
display.window.mainloop()
