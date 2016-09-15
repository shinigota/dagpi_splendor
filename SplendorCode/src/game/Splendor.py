from src.mvc.Display import Display
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Splendor:
    game_board = None
    game_rules = None
    display = None

    def __init__(self):
        self.display = Display()
        self.display.game_board = GameBoard(self.display,
                                                            GameRules())
        self.display.game_rules = self.display.game_board.game_rules
        self.display.game_rules.game_board = self.display.game_board
        self.display.game_rules.display = self.display
        self.display.create_window()
        self.display.launch()
        self.display.window.mainloop()



Splendor()