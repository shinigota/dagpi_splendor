# Functional specifications
---

## GameBoard
	## Variables ##
	types = []
	hiddenTiles = []
	displayedTiles = []
	deck = []
	displayedCards = []

	## Functions / Proceedings ##
	def addType(self, type): 
	def delTypes(self, type):
	def countTypes(self):
	def addHiddenTile(self, tile):
	def delHiddenTile(self, tile):
	def addDisplayedTile(self, tile):
	def delDisplayedTile(self, tile):
	def addToDeck(self, card):
	def delToDeck(self, card):
	def addDisplayedCard(self, card):
	def delDisplayedCard(self, card):
	
	
## GameRules
	## Variables ##
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
	
	## Functions / Proceedings ##
	
	
## Display
	 ##Variables ##
	
	
	## Functions / Proceedings ##
	
	
## RessourceType
	## Variables ##
	name = None
	
	## Functions / Proceedings ##
	
	
## Tile
	## Variables ##
	points = None
	type = None
	gemsConditions = []
	
	## Functions / Proceedings ##
	def setPoints(self, points):
	def getPoints(self):
	def setType(self, type):
	def getType(self):
	def addGemsConditions(self, tokenStack):
	def delGemsConditions(self, tokenStack):
	def getGemsConditions(self):

	
## TokenStack
	## Variables ##
	nbToken = None
    type = None
	
	## Functions / Proceedings ##
	
	
## Card
	## Variables ##
	points = None
	incomeGem = None
	purchaseGems =[]
	
	## Functions / Proceedings ##
	def setIncomeGem(self, tokenStack):
	def addPurchaseGems(self, tokenStack):
	def delPurchaseGems(self, tokenStack):

	
## Player
	## Variables ##
	purchasedCards = []
	reservedCards = []
	ownedTiles = []
	bank = []
	position = None
	nickname = None
	
	
	## Functions / Proceedings ##
	def initBank(self, type): - Initialize the player token bank
	def addPurchasedCard(self, card): - Add to the player, a card bought
	def delPurchasedCard(self, card): - Delete to the player, a card owned
	def addReservedCard(self, card): - Add to the player, a card reserved
	def delReservedCard(self, card): - Delete to the player, a card reserved
	def addOwnedTile(self, tile): - Add to the player, a tile
	def delOwnedTile(self, tile): - Delete to the player, a tile
	
	
## AI