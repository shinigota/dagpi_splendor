from src.element.Token import Token
from src.mvc.GameRules import GameRules


class GameBoard:
    def __init__(self):

        gameRules = GameRules()
        self.types = []
        nbPlayers = 0
        nbGems = 2

        if nbPlayers == 2:
            nbGems = gameRules.nb_gem_for_2
        elif nbPlayers == 3:
            nbGems = gameRules.nb_gem_for_3
        else:
            nbGems = gameRules.nb_gem_for_4

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
        tkStack = Token()
        tkStack.type = type
        tkStack.nb_token = nbGems
        return tkStack

    def purchase_card(self, card):
        None
        # player.purchase_card(card)
        # add new card to gameboard, delete one from stack

        # display.update()

    # def click_token(self, token):
    #
    #     if player.is_player_token(token):
    #         player.give_back_token(token)
    #         self.token_stacks[token.type].add_token()
    #         self.token_took - -
    #     elif self.is_gameboard_token(token):
    #         player.take_token(token)
    #         self.token_stacks[token.type].remove_token()
    #         self.token_took + +
    #
    #     if self.token_took == 3:
    #         next_turn()
    #
    #     update_view()
