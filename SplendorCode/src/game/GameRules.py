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
    nbMinGemStack = 0

    def __init__(self, gameboard):
        gameboard.rien = 0
        tree = ET.parse("../res/splendor_res.xml")
        root = tree.getroot()
        print()
        # Single parameter xml
        for sp in root.findall('single_parameters'):
            self.gameName = sp.find('game_name').text
            self.nbLvlCard = sp.find('number_levels_cards').text
            self.nbMaxResCard = sp.find('number_max_reserved_cards').text
            self.nbPointsTile = sp.find('number_prestige_points_noble_tiles').text
            self.nbPointsEnd = sp.find('number_prestige_points_end_game').text

        # Token xml
        for token in root.findall(".//token"):
            nameT = token.find('name').text
            colorT = token.find('color').text
            print(nameT, colorT)
        print()

        # Game setup xml
        for gs in root.findall('game_setup'):
            self.nbCardReveal = gs.find('number_cards_to_reveal').text
            self.nbTilesnbP = gs.find('number_noble_tiles_more_number_players').text
            ngtiganp = './/number_gem_tokens_in_game_according_number_players'
            for ngtigan in root.findall(ngtiganp):
                self.nbGemFor2 = ngtigan.find('number_gem_tokens_in_game_2_players').text
                self.nbGemFor3 = ngtigan.find('number_gem_tokens_in_game_3_players').text
                self.nbGemFor4 = ngtigan.find('number_gem_tokens_in_game_4_players').text
            self.nbGold = gs.find('number_gold_tokens_in_game').text

        # Turn parameters xml
        for tp in root.findall('turn_parameters'):
            self.nbGemDiff = tp.find('number_gem_tokens_different_colors').text
            self.nbGemSame = tp.find('number_gem_tokens_same_color').text
            nmgtsisc = 'number_min_gem_tokens_stack_if_same_color'
            self.nbMinGemStack = tp.find(nmgtsisc).text
            nmgticr = 'number_max_gold_tokens_if_card_reserved'
            self.nbGoldTake = tp.find(nmgticr).text
            self.nbTokenEndTurn = tp.find('number_max_tokens_end_turn').text
            self.nbTilePerTurn = tp.find('number_max_noble_tile_turn').text


        # Noble tiles xml
        for noble_tile in root.findall('.//noble_tile'):
            nt_emerald = noble_tile.find('Emerald').text
            nt_diamond = noble_tile.find('Diamond').text
            nt_sapphire = noble_tile.find('Sapphire').text
            nt_onyx = noble_tile.find('Onyx').text
            nt_ruby = noble_tile.find('Ruby').text

        # Development cards xml
        for dc in root.findall('.//development_card'):
            level = dc.find('level').text
            c_emerald = dc.find('Emerald').text
            c_diamond = dc.find('Diamond').text
            c_sapphire = dc.find('Sapphire').text
            c_onyx = dc.find('Onyx').text
            c_ruby = dc.find('Ruby').text
            number_prestige_points = dc.find('number_prestige_points').text
            gem_token_bonus = dc.find('gem_token_bonus').text
