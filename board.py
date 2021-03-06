from utils import get_position_with_row_col

class Board:
    def __init__(self, pieces, color_up):
        # Example: [Piece('12WND'), Piece('14BNU'), Piece('24WYD')]
        self.pieces = pieces
        self.color_up = color_up # Defines which of the colors is moving up.
    
    def get_color_up(self):
        return self.color_up

    def get_pieces(self):
        return self.pieces

    def get_piece_by_index(self, index):
        return self.pieces[index]

    def has_piece(self, position):
        # Receives position (e.g.: 28), returns True if there's a piece in that position
        string_pos = str(position)

        for piece in self.pieces:
            if piece.get_position() == string_pos:
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
    
    def get_row(self, row_number):
        # Receives a row number, returns a set with all pieces contained in it.
        # [0, 1, 2, 3] represents the first row of the board. All rows contain four squares.
        # row_pos needs to contain strings on it because Piece.get_position() returns a number in type string.

        row_pos = [0, 1, 2, 3]
        row_pos = list(map((lambda pos: str(pos + (4 * row_number))), row_pos))
        row = []

        for piece in self.pieces:
            if piece.get_position() in row_pos:
                row.append(piece)

        return set(row)
    
    def get_pieces_by_coords(self, *coords):
        # Receives a variable number of (row, column) pairs.
        # Returns a ordered list of same length with a Piece if found, otherwise None.
        row_memory = dict() # Used to not have to keep calling get_row().
        results = []

        for coord_pair in coords:
            if coord_pair[0] in row_memory:
                current_row = row_memory[coord_pair[0]]
            else:
                current_row = self.get_row(coord_pair[0])
                row_memory[coord_pair[0]] = current_row
            
            for piece in current_row:
                if self.get_col_number(int(piece.get_position())) == coord_pair[1]:
                    results.append(piece)
                    break
            else:
                # This runs if 'break' isn't called on the for loop above.
                results.append(None)
        
        return results
    
    def move_piece(self, index, new_position):
        def is_eat_movement(current_position):
            # If the difference in the rows of the current and next positions isn't 1, i.e. if the piece isn't moving one square, 
            # then the piece is eating another piece.
            return abs(self.get_row_number(current_position) - self.get_row_number(new_position)) != 1

        def get_eaten_index(current_position):
            current_coords = [self.get_row_number(current_position), self.get_col_number(current_position)]
            new_coords = [self.get_row_number(new_position), self.get_col_number(new_position)]
            eaten_coords = [current_coords[0], current_coords[1]]

            # Dividing by 2 because neither the current position or the new one is desired, but the one in the middle.
            # Getting the difference between the new coordinates and current coordinates helps getting the direction.
            eaten_coords[0] += (new_coords[0] - current_coords[0]) // 2
            eaten_coords[1] += (new_coords[1] - current_coords[1]) // 2

            # Converting to string to compare later.
            eaten_position = str(get_position_with_row_col(eaten_coords[0], eaten_coords[1]))

            for index, piece in enumerate(self.pieces):
                if piece.get_position() == eaten_position:
                    return index

        piece_to_move = self.pieces[index]

        # Delete piece from the board if this move eats another piece
        if is_eat_movement(int(piece_to_move.get_position())):
            self.pieces.pop(get_eaten_index(int(piece_to_move.get_position()))) 

        # Actually move
        piece_to_move.set_position(new_position)