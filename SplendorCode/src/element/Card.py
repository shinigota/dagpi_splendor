class Card:
    points = None
    income_gem = None
    purchase_gems = None

    def __init__(self, points, income_gem, purchase_gems):
        self.points = points
        self.income_gem = income_gem
        self.purchase_gems = purchase_gems

    def set_income_gem(self, token_stack):
        self.income_gem = token_stack

    def add_purchase_gems(self, token_stack):
        self.purchase_gems.append(token_stack)

    def del_purchase_gems(self, token_stack):
        self.purchase_gems.remove(token_stack)
        del token_stack
