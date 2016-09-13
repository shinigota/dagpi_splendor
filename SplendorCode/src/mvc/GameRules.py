import xml.etree.ElementTree as ET

from src.element.RessourceType import RessourceType
from src.mvc.EventType import EventType


class GameRules:
    game_name = ""
    nb_lvl_card = 0
    nb_max_res_card = 0
    nb_points_tile = 0
    nb_points_end = 0
    nb_card_reveal = 0
    nb_tile_more = 0
    nb_gem_for_2 = 0
    nb_gem_for_3 = 0
    nb_gem_for_4 = 0
    nb_gold = 0
    nb_gem_dif = 0
    nb_gem_same = 0
    nb_gold_take = 0
    nb_token_end_turn = 0
    nb_tile_per_turn = 0
    nb_min_gem_stack = 0
    development_cards = 0
    game_board = None
    display = None
    tiles = None

    def __init__(self):
        tree = ET.parse("../res/splendor_res.xml")
        root = tree.getroot()
        # Single game_board xml
        for sp in root.findall('single_parameters'):
            GameRules.game_name = sp.find('game_name').text
            GameRules.nb_lvl_card = sp.find('number_levels_cards').text
            GameRules.nb_max_res_card = sp.find(
                'number_max_reserved_cards').text
            GameRules.nb_points_tile = sp.find(
                'number_prestige_points_noble_tiles').text
            GameRules.nb_points_end = sp.find(
                'number_prestige_points_end_game').text

        # Token xml
        for token in root.findall(".//token"):
            name_t = token.find('name').text
            color_t = token.find('color').text
            RessourceType.add_ressource(name_t, color_t)

        # Game setup xml
        for gs in root.findall('game_setup'):
            GameRules.nb_card_reveal = gs.find('number_cards_to_reveal').text
            GameRules.nb_tiles_nb_p = gs.find(
                'number_noble_tiles_more_number_players').text
            ngtiganp = './/number_gem_tokens_in_game_according_number_players'
            for ngtigan in root.findall(ngtiganp):
                GameRules.nb_gem_for_2 = ngtigan.find(
                    'number_gem_tokens_in_game_2_players').text
                GameRules.nb_gem_for_3 = ngtigan.find(
                    'number_gem_tokens_in_game_3_players').text
                GameRules.nb_gem_for_4 = ngtigan.find(
                    'number_gem_tokens_in_game_4_players').text
                GameRules.nb_gold = gs.find('number_gold_tokens_in_game').text

        # Turn parameters xml
        for tp in root.findall('turn_parameters'):
            GameRules.nbGemDiff = tp.find(
                'number_gem_tokens_different_colors').text
            GameRules.nb_gem_same = tp.find(
                'number_gem_tokens_same_color').text
            nmgtsisc = 'number_min_gem_tokens_stack_if_same_color'
            GameRules.nb_min_gem_stack = tp.find(nmgtsisc).text
            nmgticr = 'number_max_gold_tokens_if_card_reserved'
            GameRules.nb_gold_take = tp.find(nmgticr).text
            GameRules.nb_token_end_turn = tp.find(
                'number_max_tokens_end_turn').text
            GameRules.nb_tile_per_turn = tp.find(
                'number_max_noble_tile_turn').text

        # Noble tiles xml
        GameRules.tiles = []
        for noble_tile in root.findall('.//noble_tile'):
            nt_emerald = noble_tile.find('Emerald').text
            nt_diamond = noble_tile.find('Diamond').text
            nt_sapphire = noble_tile.find('Sapphire').text
            nt_onyx = noble_tile.find('Onyx').text
            nt_ruby = noble_tile.find('Ruby').text

            GameRules.tiles.append({
                "emerald": nt_emerald,
                "diamond": nt_diamond,
                "sapphire": nt_sapphire,
                "onyx": nt_onyx,
                "ruby": nt_ruby
            })

        # Development cards xml
        GameRules.development_cards = {}
        for i in range(1, int(self.nb_lvl_card) + 1):
            GameRules.development_cards[i] = []

        for dc in root.findall('.//development_card'):
            level = dc.find('level').text
            c_emerald = dc.find('Emerald').text
            c_diamond = dc.find('Diamond').text
            c_sapphire = dc.find('Sapphire').text
            c_onyx = dc.find('Onyx').text
            c_ruby = dc.find('Ruby').text
            number_prestige_points = dc.find('number_prestige_points').text
            gem_token_bonus = dc.find('gem_token_bonus').text

            GameRules.development_cards[int(level)].append({
                "level": level,
                "number_prestige_points": number_prestige_points,
                "gem_token_bonus": gem_token_bonus,
                "cost": {
                    "emerald": c_emerald,
                    "diamond": c_diamond,
                    "sapphire": c_sapphire,
                    "onyx": c_onyx,
                    "ruby": c_ruby
                }
            })
            print(int(level))

    def event(self, event_type, object):
        action_possible = False
        if event_type == EventType.CLICK_TAKE_TOKEN_GAMEBOARD:
            # action_possible = self.check_click_token(object)
            if action_possible:
                self.game_board.click_token_game_board(object)
        elif event_type == EventType.CLICK_GIVE_BACK_PLAYER_TOKEN:
            # action_possible =
            if action_possible:
                self.game_board.click_token_player(object)
        elif event_type == EventType.CLICK_DISPLAYED_CARD:
            # action_possible =
            if action_possible:
                self.game_board.click_displayed_card(object)
        elif event_type == EventType.CLICK_DECK_CARD:
            # action_possible =
            if action_possible:
                self.game_board.click_card_deck(object)
        elif event_type == EventType.CANCEL_ACTION:
            # action_possible =
            if action_possible:
                pass
        elif event_type == EventType.VALIDATE_ACTION:
            # action_possible =
            if action_possible:
                pass
        elif event_type == EventType.CLICK_TILE:
            # action_possible =
            if action_possible:
                self.game_board.click_tile(object)
        elif event_type == EventType.START:
            # action_possible =
            if action_possible:
                pass
        elif event_type == EventType.EXIT:
            # action_possible =
            if action_possible:
                pass
        elif event_type == EventType.POPUP_PURCHASE:
            # action_possible =
            if action_possible:
                self.game_board.click_purchase_card(object)
        elif event_type == EventType.POPUP_RESERVE:
            # action_possible =
            if action_possible:
                self.game_board.click_reserve_card(object)

        return action_possible

    def get_development_cards(self):
        return self.development_cards

    def check_click_token(self):
        return

    def check_click_card(self):
        return

    def check_click_tile(self):
        return

    def check_winner(self, player):
        for n_player in player.name:
            if n_player.calcul_point_in_game() >= GameRules.nb_points_end:
                return n_player

    def check_enough_ressources(self):
        return True

    def check_reserve_amount(self):
        return True

    def get_tiles(self):
        return self.tiles

    def set_game_board(self, game_board):
        self.game_board = game_board

    def set_display(self, display):
        self.display = display
