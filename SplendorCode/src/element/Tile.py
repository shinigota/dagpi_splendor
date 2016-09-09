from src.element.GemStack import GemStack


class Tile:
    points = None
    gem_conditions = None

    def __init__(self, pts,  gem_conditions):
        self.points = pts
        self.gems_conditions = gem_conditions

    def get_points(self):
        return self.points

    def get_gem_conditions(self):
        return self.gem_conditionss

    def visit_player(self, player):
        player.add_owned_tile(self)