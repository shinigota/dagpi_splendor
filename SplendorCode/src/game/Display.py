from tkinter import *

from src.game.GameRules import GameRules


class Display:
    """zerghj."""
    window = None
    text = "test"
    isshow = True;
    w, h = None, None

    def __init__(self):
        """dfgh."""
        self.window = Tk()
        self.createwindow()  # fghj

    def createwindow(self):
        self.window.title(GameRules.game_name)
        # self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.w, self.h = 1900, 1000
        self.window.overrideredirect(0)
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))

    def displaytile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100, background='#c18b01')
        txt = canvas.create_text(10, 10, text=0, fill="black")
        txt = canvas.create_text(50, 10, text="R", fill="red")
        canvas.place(x=250 + 120 * (position - 1), y=120, anchor=SE)


GameRules()
display = Display()
display.displaytile(1, None)
display.displaytile(2, None)
display.displaytile(3, None)
display.displaytile(4, None)
display.window.mainloop()
