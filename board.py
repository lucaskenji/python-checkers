class Board:
    def __init__(self, pieces):
        # Example: [12WN, 14BN, 24WY]
        self.pieces = pieces
    
    def has_piece(self, position):
        # Receives position (ex: 28), returns True if there's a piece in that position
        for piece in pieces:
            if piece[:-2] == position:
                return True

        return False