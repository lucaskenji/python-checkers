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
        def get_eat_position(piece, coords):
            if (piece.get_color() == self.get_color()) or (coords[0] in (0, 7)) or (coords[1] in (0, 7)):
                return None

            if coords[1] > current_col:
                position_to_eat = (coords[0] + (coords[0] - current_row), coords[1] + 1)
            else:
                position_to_eat = (coords[0] + (coords[0] - current_row), coords[1] - 1)
            
            position_num = (position_to_eat[0] * 4) + (position_to_eat[1] // 2)
            return None if board.has_piece(position_num) else position_num

        current_col = board.get_col_number(int(self.get_position()))
        current_row = board.get_row_number(int(self.get_position()))
        possible_moves = []
        own_color = self.get_color()

        if self.is_king():
            possible_coords = [(current_row - 1, current_col - 1), (current_row - 1, current_col + 1), (current_row + 1, current_col - 1), (current_row + 1, current_col + 1)]
        else:
            possible_coords = [(current_row - 1, current_col - 1), (current_row - 1, current_col + 1)] if board.get_color_up() == self.get_color() else [(current_row + 1, current_col - 1), (current_row + 1, current_col + 1)]

        possible_coords = list(filter(lambda coords: coords[0] != -1 and coords[0] != 8 and coords[1] != -1 and coords[1] != 8, possible_coords))

        close_squares = board.get_pieces_by_coords(*possible_coords)
        empty_squares = []

        for index, square in enumerate(close_squares):
            if square is None:
                empty_squares.append(index)
            else:
                position_to_eat = get_eat_position(square, possible_coords[index])
                if position_to_eat is None:
                    continue
                
                possible_moves.append(str(position_to_eat))

        if len(possible_moves) == 0:
            for index in empty_squares:
                new_position = (possible_coords[index][0] * 4) + (possible_coords[index][1] // 2)
                possible_moves.append(str(new_position))
        
        return set(possible_moves)