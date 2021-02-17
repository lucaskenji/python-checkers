class Board:
    def __init__(self, pieces):
        # Example: [12WN, 14BN, 24WY]
        self.pieces = pieces
    
    def has_piece(self, position):
        # Receives position (e.g.: 28), returns True if there's a piece in that position
        string_pos = str(position)

        for piece in self.pieces:
            if piece[:-2] == string_pos:
                return True

        return False
    
    def get_row_number(self, position):
        # Receives position (e.g.: 1), returns the row this position is on the board.
        return position // 4
    
    def get_col_number(self, position):
        # There are four dark squares on each row where pieces can be placed.
        # The remainder of (position / 4) can be used to determine which of the four squares has the position.
        # We also take into account that odd rows on the board have a offset of 1 column.
        remainder = position % 4
        column_position = remainder * 2 # because the squares have a gap of one light square.
        is_row_odd = not (self.get_row_number(position) % 2 == 0)
        return column_position + 1 if is_row_odd else column_position