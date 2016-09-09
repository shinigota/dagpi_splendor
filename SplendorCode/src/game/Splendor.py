from src.mvc.Display import Display
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules


class Splendor:
    gameboard = None
    gamerules = None
    display = None

    def __init__(self):
        gameboard = GameBoard()
        gamerules = GameRules(gameboard)
        display = Display(gamerules, gameboard)


Splendor()