from src.element.ResourceType import ResourceType


class Token:
    type = None

    def __init__(self, type):
        self.type = type

    def get_color(self):
        print('Token -- get_color')
        return ResourceType.get_ressource_color(self.type)

    def get_type(self):
        print('Token -- get_type')
        return self.type
