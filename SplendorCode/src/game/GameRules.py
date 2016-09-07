from src.game.GameBoard import GameBoard


class GameRules:
    gameName = ""
    nbLvlCard = 0
    nbMaxResCard = 0
    nbPointsTile = 0
    nbCardReveal = 0
    nbTileMore = 0
    nbGemFor2 = 0
    nbGemFor3 = 0
    nbGemFor4 = 0
    nbGold = 0
    nbGemDif = 0
    nbGemSame = 0
    nbGoldTake = 0
    nbTokenEndTurn = 0
    nbTilePerTurn = 0

    def __init__(self, gameboard):
        gameboard.rien = 0
