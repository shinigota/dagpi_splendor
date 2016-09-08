class Tile:
    points = None
    gems_conditions = None

    def __init__(self):
        self.points = None
        self.gems_conditions = []

    def setPoints(self, points):
        self.points = points

    def getPoints(self):
        return self.points

    def add_gems_conditions(self, token_stack):
        self.gems_conditions.append(token_stack)

    def del_gems_conditions(self, token_stack):
        self.gems_conditions.remove(token_stack)
        del token_stack

    def get_gems_conditions(self):
        return self.gems_conditions
