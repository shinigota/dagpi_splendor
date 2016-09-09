from tkinter import *

from src.element.Card import Card
from src.game.GameRules import GameRules
from src.game.EventType import EventType


class Display:
    """zerghj."""
    window = None
    text = "test"
    game_rules = None
    w = None
    h = None

    def __init__(self):
        """dfgh."""
        self.window = Tk()

    def create_window(self):
        self.window.title(GameRules.game_name)
        self.w, self.h = 1900, 1000
        self.window.overrideredirect(0)
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))

    def display_tile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100, background='#c18b01')
        points = canvas.create_text(10, 10, text=0, fill="black")
        cardBuy1 = canvas.create_rectangle(10, 25, 40, 55, fill="red")
        cardBuy2 = canvas.create_rectangle(10, 65, 40, 95, fill="blue")
        cardBuy3 = canvas.create_rectangle(60, 65, 90, 95, fill="green")
        txtBuy1 = canvas.create_text(25, 40, text="0", fill="white")
        txtBuy2 = canvas.create_text(25, 80, text="0", fill="white")
        txtBuy3 = canvas.create_text(75, 80, text="0", fill="white")
        canvas.place(x=250 + 120 * (position - 1), y=150, anchor=SE)
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_TILE, t=tile: self.game_rules.event(e, t))

    def display_card(self, position, card):
        canvas = Canvas(self.window, width=100, height=120, background=self.get_color(card.level))
        points = canvas.create_text(10, 10, text=0, fill="black")
        gem = canvas.create_oval(85, 5, 95, 15, fill=card.income_gem)
        gemBuy1 = canvas.create_oval(10, 85, 40, 115, fill=card.income_gem)
        gemBuy2 = canvas.create_oval(60, 85, 90, 115, fill=card.income_gem)
        gemBuy3 = canvas.create_oval(10, 45, 40, 75, fill=card.income_gem)
        gemBuy4 = canvas.create_oval(60, 45, 90, 75, fill=card.income_gem)
        txtBuy1 = canvas.create_text(25, 100, text=0, fill="white")
        txtBuy2 = canvas.create_text(75, 100, text=0, fill="white")
        txtBuy3 = canvas.create_text(25, 60, text=0, fill="white")
        txtBuy4 = canvas.create_text(75, 60, text=0, fill="white")
        canvas.place(x=250 + 120 * (position - 1), y=300 + (130 * (card.level - 1)), anchor=SE)
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_CARD, c=card: self.game_rules.event(e, c))

    def display_pile(self, level):
        canvas = Canvas(self.window, width=100, height=120, background=self.get_color(level))
        canvas.create_text(50, 50, text="PILE", fill="black")
        canvas.place(x=120, y=300 + (130 * (level - 1)), anchor=SE)

    def display_gold(self, nb):
        canvas = Canvas(self.window, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70, fill="yellow")
        canvas.create_text(40, 40, text=nb, fill="black")
        canvas.place(x=115, y=135, anchor=SE)

    def display_gem(self, nb):
        canvas = Canvas(self.window, width=80, height=80)
        canvas.create_oval(10, 10, 70, 70, fill="yellow")
        canvas.create_text(40, 40, text=nb, fill="black")
        canvas.place(x=115, y=135, anchor=SE)

    def get_color(self, level):
        if level == 1:
            color = '#0483f9'
        if level == 2:
            color = '#05e002'
        if level == 3:
            color = '#ffac07'
        return color


display = Display()
display.game_rules = GameRules()
display.create_window()
display.display_tile(1, None)
display.display_tile(2, None)
display.display_tile(3, None)
display.display_tile(4, None)
display.display_tile(5, None)

card1 = Card(0, "red", 0, 1)
card2 = Card(0, "black", 0, 2)
card3 = Card(0, "blue", 0, 3)

display.display_card(1, card1)
display.display_card(2, card1)
display.display_card(3, card1)
display.display_card(4, card1)
display.display_card(1, card2)
display.display_card(2, card2)
display.display_card(3, card2)
display.display_card(4, card2)
display.display_card(1, card3)
display.display_card(2, card3)
display.display_card(3, card3)
display.display_card(4, card3)

display.display_pile(1)
display.display_pile(2)
display.display_pile(3)

display.display_gold(5)

display.window.mainloop()
