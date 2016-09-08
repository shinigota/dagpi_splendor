from tkinter import *

from src.game.GameRules import GameRules


class Display:
    def __init__(self):
        self.app = Tk()
        self.createwindow()

    def createwindow(self):
        self.app.title(GameRules.game_name)
        w, h = self.app.winfo_screenwidth(), self.app.winfo_screenheight()
        self.app.overrideredirect(1)
        self.app.geometry("%dx%d+0+0" % (w, h))
        self.app.mainloop()


Display()