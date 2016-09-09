from src.player.Player import Player


class AI(Player):

    def __init__(self, position, difficulty):
        Player.__init__()
        self.dificulty = difficulty
        self.position = position
