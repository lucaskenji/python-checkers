class Piece:
    def __init__(self, name):
        # Example: <position><color><isKing?> 16WN
        self.name = name
    
    def getPosition(self):
        return self.name[:-2]

    def getColor(self):
        return self.name[-2]

    def isKing(self):
        return True if self.name[-1] == 'Y' else False