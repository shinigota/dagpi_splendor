# Functional specifications
---

## GameBoard
	## Variables ##
	types = []
	hidden_tiles = []
	displayed_tiles = []
	deck = []
	displayed_cards = []

	## Functions / Proceedings ##
	add_type(self, type):
	del_types(self, type)
	count_types(self)
	add_hidden_tile(self, tile)
	del_hidden_tile(self, tile)
	add_displayed_tile(self, tile)
	del_displayed_tile(self, tile)
	add_to_deck(self, card)
	del_to_deck(self, card)
	add_displayed_dard(self, card)
	del_displayed_card(self, card)
	click_token(self, token)
	
	
## GameRules
	## Variables ##
	game_name = ""
    nb_lvl_card = 0
    nb_max_res_card = 0
    nb_points_tile = 0
    nb_card_reveal = 0
    nb_tile_more = 0
    nb_gem_for2 = 0
    nb_gem_for3 = 0
    nb_gem_for4 = 0
    nb_gold = 0
    nb_gem_dif = 0
    nb_gem_same = 0
    nb_gold_take = 0
    nb_token_end_turn = 0
    nb_tile_per_turn = 0
	
	## Functions / Proceedings ##
	
	
## Display
	## Variables ##
	
	
	## Functions / Proceedings ##

## EventType
	## Values ##
    START
    EXIT
    SAVE_GAME_PARAMETERS - Param : parameters
    CLICK_DISPLAYED_CARD - Param : card
    CLICK_DECK_CARD - Param : card
    CLICK_TOKEN - Param : token
    CLICK_TILE - Param : tile
    POPUP_PURCHASE - Param : Card
    POPUP_RESERVE - Param : Card
    CANCEL_ACTION
    VALIDATE_ACTION


	
## RessourceType
	## Variables ##
	name = None
	
	## Functions / Proceedings ##
	
	
## Tile
	## Variables ##
	points = None
	type = None
	gems_conditions = []
	
	## Functions / Proceedings ##
	set_points(self, points)
	get_points(self)
	set_type(self, type)
	get_type(self)
	add_gems_conditions(self, token_stack)
	del_gems_conditions(self, token_stack)
	get_gems_conditions(self)

	
## TokenStack
	## Variables ##
	nb_token = None
    type = None
	
	## Functions / Proceedings ##
	
	
## Card
	## Variables ##
	points = None
	income_gem = None
	purchase_gems =[]
	
	## Functions / Proceedings ##
	set_income_gem(self, token_stack)
	add_purchase_gems(self, token_stack)
	del_purchase_gems(self, token_stack)

	
## Player
    HEAD

	## Variables ##
	purchased_cards = []
	reserved_cards = []
	owned_tiles = []
	bank = []
	position = None
	nickname = None
	
	
	## Functions / Proceedings ##
	init_bank(self, type) - Initialize the player token bank
	add_purchased_card(self, card) - Add to the player, a card bought
	del_purchased_card(self, card) - Delete to the player, a card owned
	add_reserved_card(self, card) - Add to the player, a card reserved
	del_reserved_card(self, card) - Delete to the player, a card reserved
	add_owned_tile(self, tile) - Add to the player, a tile
	del_owned_tile(self, tile) - Delete to the player, a tile

## AI
* Focusing on a specific strategy
  * Winning nobles by purchasing cheap cards
  * Buying expensive card, targeting a lot of points
* Examinating all **his** next **X** *(depth)* turns, choosing the best path leading to the strategy
  * Depth determines the AI's difficulty
* AI based on early game, mid game, end game times
  * AI's income (from mines) determines the state of the game
  * AI begins by reserving a tier 3 card
  * Based on the card's cost to value ratio, AI will
  	* (5 points) Tiles strategy, until late game, then buy its reserved card
  	* (4 points) If the cost is low, tiles strategy and buy the card in the end game. Otherwise, tiles strategy and gnot obliged to buy the card
  	* (3 points) Tiles strategy
