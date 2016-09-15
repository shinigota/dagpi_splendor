from src.game.GameState import GameState


class GameStateString:
    TEXT = {}
    TEXT[GameState.PLAYER_TURN.value] = "%s, jouez !"
    TEXT[GameState.PLAYER_GIVE_TOKENS_BACK.value] = "%s, vous avez des " \
                                                    "jetons en " \
                                              "trop !"
    TEXT[GameState.CANNOT_PLAY.value] = "%s, vous ne pouvez pas jouer, " \
                                        "votre tour " \
                                  "est passé !"
    TEXT[GameState.END.value] = "%s, vous ne pouvez pas jouer, " \
                                        "votre tour " \
                                  "est passé !"

    # TEXT[GameState.PLAYER_CHOOSE_PURHCASE_OR_RESERVE] = ""
    # TEXT[GameState.PLAYER_CHOOSE_TILE] = ""

    @staticmethod
    def get_text(game_state, arg):
        return GameStateString.TEXT[game_state.value] % (arg)

