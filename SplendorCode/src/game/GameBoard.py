from src.element.Tile import Tile
from src.element.Card import Card
from src.element.RessourceType import Type
from src.element.TokenStack import TokenStack

from GameRules import GameRules

class GameBoard:

    def __init__(self):

        gameRules = GameRules()
        self.types = []
        nbPlayers = 0
        nbGems = 2


        if nbPlayers == 2:
            nbGems = gameRules.nbGemFor2
        elif nbPlayers == 3:
            nbGems = gameRules.nbGemFor3
        else:
            nbGems = gameRules.nbGemFor4


        for type in self.types:
            self.initTokenStack(type, nbGems)

        



        self.hiddenTiles = []
        self.displayedTiles = []
        self.deck = []
        self.displayedCards = []



    def addType(self, type):
        self.types.append(type)

    def delTypes(self, type):
        self.types.remove(type)
        del type

    def countTypes(self):
        return len(self.types)




    def addHiddenTile(self, tile):
        self.hiddenTiles.append(tile)

    def delHiddenTile(self, tile):
        self.hiddenTiles.remove(tile)



    def addDisplayedTile(self, tile):
        self.displayedTiles.append(tile)

    def delDisplayedTile(self, tile):
        self.displayedTiles.remove(tile)



    def addToDeck(self, card):
        self.deck.append(card)

    def delToDeck(self, card):
        self.deck.remove(card)



    def addDisplayedCard(self, card):
        self.displayedCards.append(card)

    def delDisplayedCard(self, card):
        self.displayedCards.remove(card)


    def initTokenStack(self, type, nbGems):
        tkStack = TokenStack()
        tkStack.type = type
        tkStack.nbToken = nbGems
        return tkStack

