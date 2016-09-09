from enum import Enum


class RessourceType:
    ressource_type = None

    def __init__(self):
        self.ressource_type = dict()

    def add_ressource(self, name, color):
        self.ressource_type[name] = color

    def get_ressource_color(self, name):
        return self.ressource_type[name]


