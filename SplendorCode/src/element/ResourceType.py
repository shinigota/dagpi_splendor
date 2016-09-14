from enum import Enum


class ResourceType:
    resource_type = dict()

    # def __init__(self):
    #     RessourceType.ressource_type = dict()

    @staticmethod
    def add_resource(name, color):
        ResourceType.resource_type[name] = color

    @staticmethod
    def get_color(name):
        return ResourceType.resource_type[name]

    @staticmethod
    def get_sorted_resources():
        return sorted(ResourceType.resource_type)
