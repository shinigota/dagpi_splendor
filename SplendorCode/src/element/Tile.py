from src.element.GemStack import GemStack


class Tile:

    def __init__(self, pts, type, gem_stacks):
        self.points = pts
        self.type = type
        self.gems_conditions = [GemStack]

        for gem_stack in gem_stacks:
            self.add_gems_conditions(self, gem_stack)


    def add_gems_conditions(self, gem_stack):
        self.gems_conditions.append(gem_stack)

    def del_gems_conditions(self, gem_stack):
        self.gems_conditions.remove(gem_stack)
        del gem_stack

    def get_gems_conditions(self):
        return self.gems_conditions
