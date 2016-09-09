


class Card:
    points = None
    income_gem = None
    purchase_gems = None
    level = None

    def __init__(self, points, income_gem, purchase_gems, level):
        self.points = points
        self.income_gem = income_gem
        self.purchase_gems = purchase_gems
        self.level = level

    def get_purchase_gems(self):
        return self.purchase_gems

    def get_income_gem(self):
        return self.income_gem

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points