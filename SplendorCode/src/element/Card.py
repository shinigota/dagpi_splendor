from src.element.GemStack import GemStack


class Card:
    points = None
    income_gem = None
    purchase_gems = None
    level = None

    def __init__(self, points, income_gem, purchase_gems, level):
        self.points = points
        self.income_gem = income_gem
        self.purchase_gems = [GemStack]
        self.purchase_gems = purchase_gems
        self.level = level

    def set_income_gem(self, token_stack):
        self.income_gem = token_stack

    def add_purchase_gems(self, gem_stack):
        self.purchase_gems.append(gem_stack)

    def del_purchase_gems(self, gem_stack):
        self.purchase_gems.remove(gem_stack)
        del gem_stack
