class Tile:

    def __init__(self):
        self.points = None
        self.type = None
        self.gemsConditions = []

    def setPoints(self, points):
        self.points = points

    def getPoints(self):
        return self.points

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def addGemsConditions(self, tokenStack):
        self.gemsConditions.append(tokenStack)

    def delGemsConditions(self, tokenStack):
        self.gemsConditions.remove(tokenStack)
        del tokenStack

    def getGemsConditions(self):
        return self.gemsConditions
