from src.mvc.Display import Display
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Splendor:
    gameboard = None
    gamerules = None
    display = None

    def __init__(self):
        display = Display()
        gamerules = GameRules()
        gameboard = GameBoard(gamerules, display)
        # set gamerules gameboard




Splendor()