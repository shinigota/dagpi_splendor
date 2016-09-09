class TokenStack:
    nb_token = None
    type = None

    def __init__(self, nbToken, type):
        self.nb_token = nbToken
        self.type = type

    def addToken(self, nb_token):
        self.nb_token = self.nb_token + nb_token

    def removeToken(self, nb_token):
        self.nb_token = self.nb_token - nb_token


