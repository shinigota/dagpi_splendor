import Tools

class GameBoard:

    def __init__(self):
        self.types = []
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
