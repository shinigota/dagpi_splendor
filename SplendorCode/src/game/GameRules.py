from src.game.GameBoard import GameBoard
import xml.etree.ElementTree as ET


class GameRules:
    gameName = ""
    nbLvlCard = 0
    nbMaxResCard = 0
    nbPointsTile = 0
	nbPointsEnd = 0
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
		tree = ET.parse("splendor_res.xml")
		root = tree.getroot()
		print()

		#Single parameter xml
		for sp in root.findall('single_parameters'):
			gameName = sp.find('game_name').text
			nbLvlCard = sp.find('number_levels_cards').text
			nbMaxResCard = sp.find('number_max_reserved_cards').text
			nbPointsTile = sp.find('number_prestige_points_noble_tiles').text
			nbPointsEnd = sp.find('number_prestige_points_end_game').text	
			print("Game name = ",gameName)
			print("Number levels cards = ",nbLvlCard)
			print("Number max reserved cards = ",nbMaxResCard)
			print("Number prestige points noble tiles = ",nbPointsTile)
			print("Number prestige points end game = ",nbPointsEnd)
			print()

		#Token xml
		for token in root.findall(".//token"):
			nameT = token.find('name').text
			colorT = token.find('color').text
			print(nameT, colorT)
		print()
				
		#Game setup xml
		for gs in root.findall('game_setup'):
			nbCardReveal = gs.find('number_cards_to_reveal').text
			nbTilesnbP = gs.find('number_noble_tiles_more_number_players').text
			ngtiganp = './/number_gem_tokens_in_game_according_number_players'
			for ngtigan in root.findall(ngtiganp):
				nbGemT2P = ngtigan.find('number_gem_tokens_in_game_2_players').text
				nbGemT3P = ngtigan.find('number_gem_tokens_in_game_3_players').text
				nbGemT4P = ngtigan.find('number_gem_tokens_in_game_4_players').text
			nbGoldT = gs.find('number_gold_tokens_in_game').text
			print('Number cards to reveal = ',nbCardReveal)
			print('Number noble tiles more number players = ',nbTilesnbP)
			print('Number gem tokens in game 2 players = ',nbGemT2P)
			print('Number gem tokens in game 3 players = ',nbGemT3P)
			print('Number gem tokens in game 4 players = ',nbGemT4P)
			print('Number gold tokens in game = ',nbGoldT)
			print()

		#Turn parameters xml
		for tp in root.findall('turn_parameters'):
			nbGemTDiffColor = tp.find('number_gem_tokens_different_colors').text
			nbGemTSameColor = tp.find('number_gem_tokens_same_color').text
			nmgtsisc = 'number_min_gem_tokens_stack_if_same_color'
			nbMinGemTstackSameColor = tp.find(nmgtsisc).text
			nmgticr = 'number_max_gold_tokens_if_card_reserved'
			nbMaxGoldTCardRes = tp.find(nmgticr).text
			nbMaxTEndTurn = tp.find('number_max_tokens_end_turn').text
			nbMaxTileTurn = tp.find('number_max_noble_tile_turn').text
			print('Number gem tokens different colors = ',nbGemTDiffColor)
			print('Number gem tokens same color = ',nbGemTSameColor)
			print('Number min gem tokens stack same color = ',nbMinGemTstackSameColor)
			print('Number max gold tokens if card reserved = ',nbMaxGoldTCardRes)
			print('Number max tokens end turn = ',nbMaxTEndTurn)
			print('Number max noble tile turn = ',nbMaxTileTurn)
			
		#Noble tiles xml
		for noble_tile in root.findall('.//noble_tile'):
			nt_emerald = noble_tile.find('Emerald').text
			nt_diamond = noble_tile.find('Diamond').text
			nt_sapphire = noble_tile.find('Sapphire').text
			nt_onyx = noble_tile.find('Onyx').text
			nt_ruby = noble_tile.find('Ruby').text
			print('Noble Tile Emerald = ', nt_emerald)
			print('Noble Tile Diamond = ', nt_diamond)
			print('Noble Tile Sapphire = ', nt_sapphire)
			print('Noble Tile Onyx = ', nt_onyx)
			print('Noble Tile Ruby = ', nt_ruby)
			print()

		#Development cards xml
		for dc in root.findall('.//development_card'):
			level = dc.find('level').text
			c_emerald = dc.find('Emerald').text
			c_diamond = dc.find('Diamond').text
			c_sapphire = dc.find('Sapphire').text
			c_onyx = dc.find('Onyx').text
			c_ruby = dc.find('Ruby').text
			number_prestige_points = dc.find('number_prestige_points').text
			gem_token_bonus = dc.find('gem_token_bonus').text
			print('Card level = ', level)
			print('Card cost Emerald = ', c_emerald)
			print('Card cost Diamond = ', c_diamond)
			print('Card cost Sapphire = ', c_sapphire)
			print('Card cost Onyx = ', c_onyx)
			print('Card cost Ruby = ', c_ruby)
			print('Number prestige points = ', number_prestige_points)
			print('Gem token bonus = ', gem_token_bonus)
			print()