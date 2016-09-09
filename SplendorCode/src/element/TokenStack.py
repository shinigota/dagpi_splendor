class TokenStack:

    def __init__(self, nbToken, type):
        self.nbToken = nbToken
        self.type = type

    def addToken(self, nbToken):
        self.nbToken = self.nbToken + nbToken

    def removeToken(self, nbToken):
        self.nbToken = self.nbToken - nbToken


