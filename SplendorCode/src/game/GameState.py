from enum import Enum


class GameState(Enum):
    PLAYER_TURN = 0
    PLAYER_GIVE_TOKENS_BACK = 1
    PLAYER_CHOOSE_PURHCASE_OR_RESERVE = 2
    PLAYER_CHOOSE_TILE = 3
    CANNOT_PLAY = 4
    MODAL = False

    @staticmethod
    def toggle_modal(modal = None):
        if modal is None:
            GameState.MODAL = not GameState.MODAL
        else:
            GameState.MODAL = modal
