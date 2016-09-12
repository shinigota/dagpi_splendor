from enum import Enum


class RessourceType:
    ressource_type = dict()

    # def __init__(self):
    #     RessourceType.ressource_type = dict()

    @staticmethod
    def add_ressource(name, color):
        RessourceType.ressource_type[name] = color

    @staticmethod
    def get_ressource_color(name):
        return RessourceType.ressource_type[name]
