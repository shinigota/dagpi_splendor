class Tile:
    points = None
    gems_conditions = None

    def __init__(self, pts, gem_conditions):
        self.points = pts
        self.gems_conditions = gem_conditions

    def get_points(self):
        return self.points

    def get_gems_conditions(self):
        return self.gems_conditions

    def visit_player(self, player):
        player.add_owned_tile(self)

