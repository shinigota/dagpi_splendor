from tkinter import *

from src.element.Card import Card
from src.game.GameRules import GameRules


class Display:
    """zerghj."""
    window = None
    text = "test"
    w, h = None, None

    def __init__(self):
        """dfgh."""
        self.window = Tk()
        self.create_window()  # fghj

    def create_window(self):
        self.window.title(GameRules.game_name)
        self.w, self.h = 1900, 1000
        self.window.overrideredirect(0)
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))

    def display_tile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100, background='#c18b01')
        points = canvas.create_text(10, 10, text=0, fill="black")
        canvas.place(x=250 + 120 * (position - 1), y=150, anchor=SE)

    def display_card(self, position, card):
        canvas = Canvas(self.window, width=100, height=120, background=self.getColor(card.level))
        points = canvas.create_text(10, 10, text=0, fill="black")
        gem = canvas.create_oval(85, 5, 95, 15, fill=card.income_gem)
        canvas.place(x=250 + 120 * (position - 1), y=300 + (130 * (card.level - 1)), anchor=SE)

    def display_Pile(self, level):
        canvas = Canvas(self.window, width=100, height=120, background=self.getColor(level))
        canvas.create_text(50, 50, text="PILE", fill="Black")
        canvas.place(x=120, y=300 + (130 * (level - 1)), anchor=SE)

    def getColor(self, level):
        if level == 1:
            color = '#0483f9'
        if level == 2:
            color = '#05e002'
        if level == 3:
            color = '#ffac07'
        return color


GameRules()
display = Display()
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

display.display_Pile(1)
display.display_Pile(2)
display.display_Pile(3)

display.window.mainloop()
