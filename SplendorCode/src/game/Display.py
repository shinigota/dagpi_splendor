from tkinter import *

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
        txt = canvas.create_text(10, 10, text=0, fill="black")
        txt = canvas.create_text(50, 10, text="R", fill="red")
        canvas.place(x=250 + 120 * (position - 1), y=150, anchor=SE)

    def display_card(self, position, niveau,card):
        if niveau == 1:
            color = '#0483f9'
        if niveau == 2:
            color = '#05e002'
        if niveau == 3:
            color = '#ffac07'
        canvas = Canvas(self.window, width=100, height=120, background=color)
        txt = canvas.create_text(10, 10, text=0, fill="black")
        txt = canvas.create_text(50, 10, text="R", fill="white")
        txt = canvas.create_rectangle(50, 10, 60, 20, fill="red")
        canvas.place(x=250 + 120 * (position - 1), y=300+(130*(niveau-1)), anchor=SE)

    def display_Pile(self,niveau):
        if niveau == 1:
            color = '#0483f9'
        if niveau == 2:
            color = '#05e002'
        if niveau == 3:
            color = '#ffac07'
        canvas = Canvas(self.window, width=100, height=120, background=color)
        txt = canvas.create_text(50, 50, text="PILE",fill="Black")
        canvas.place(x=120, y=300 + (130 * (niveau - 1)), anchor=SE)


GameRules()
display = Display()
display.display_tile(1, None)
display.display_tile(2, None)
display.display_tile(3, None)
display.display_tile(4, None)
display.display_tile(5, None)

display.display_card(1, 1, None)
display.display_card(2, 1, None)
display.display_card(3, 1, None)
display.display_card(4, 1, None)
display.display_card(1, 2, None)
display.display_card(2, 2, None)
display.display_card(3, 2, None)
display.display_card(4, 2, None)
display.display_card(1, 3, None)
display.display_card(2, 3, None)
display.display_card(3, 3, None)
display.display_card(4, 3, None)

display.display_Pile(1)
display.display_Pile(2)
display.display_Pile(3)

display.window.mainloop()
