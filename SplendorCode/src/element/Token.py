from src.element.RessourceType import RessourceType


class Token:
    type = None

    def __init__(self, type):
        self.type = type

    def get_color(self):
        return RessourceType.get_ressource_color(self.type)
