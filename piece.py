class Piece:
    def __init__(self, name):
        # Example: <position><color><isKing?> 16WN
        self.name = name
    
    def get_position(self):
        return self.name[:-2]

    def get_color(self):
        return self.name[-2]

    def is_king(self):
        return True if self.name[-1] == 'Y' else False
    
    def get_moves(self, board):
        pass