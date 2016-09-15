from src.mvc.Display import Display
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Splendor:
    game_board = None
    game_rules = None
    display = None

    def __init__(self):
        self.display = Display()
        self.game_board = GameBoard(self.display, GameRules())
        self.game_rules = self.game_board.game_rules
        self.game_rules.game_board(self.game_board)
        self.game_rules.display(self.display)
        self.display.create_window()
        self.display.refresh()
        self.display.window.mainloop()



Splendor()