from src.player.Player import Player


class AI(Player):
    difficulty = None

    def __init__(self):
        Player.__init__(self)
        self.difficulty = None
