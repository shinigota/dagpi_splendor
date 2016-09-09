from src.element.RessourceType import Type
from src.element.GemStack import GemStack


class Tile:

    def __init__(self, pts, type, gem_stacks):
        self.points = pts
        self.type = type
        self.gemsConditions = [GemStack]

        for gem_stack in gem_stacks:
            self.addGemsConditions(self, gem_stack)

    def addGemsConditions(self, gem):
        self.gemsConditions.append(gem)

    def delGemsConditions(self, gem):
        self.gemsConditions.remove(gem)
        del gem

    def getGemsConditions(self):
        return self.gemsConditions



