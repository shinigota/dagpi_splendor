from src.mvc.Display import Display
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Splendor:
    game_board = None
    game_rules = None
    display = None

    def __init__(self):
        self.display = Display()
        self.game_rules = GameRules()
        self.game_board = GameBoard(self.display, self.game_rules)
        self.game_rules.set_game_board(self.game_board)
        self.game_rules.set_display(self.display)
        self.display.create_window()
        self.display.refresh()
        self.display.window.mainloop()



Splendor()