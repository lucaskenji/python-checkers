def get_piece_position(coords, square_dist, top_left_coords):
    # Receives a piece's x and y coordinates along with the GUI's specific properties, returning a piece's position (0 - 31) on the board.
    # GUI properties should be a list containing the distance in pixels of each square and the top left corner's coordinates.
    horizontal_distance = square_dist * 2
    vertical_distance = square_dist



    pass

def get_piece_gui_coords(coords, square_dist, top_left_coords):
    # Receives a piece's row and column position along with the GUI's specific properties, returning a piece's coordinates on the GUI.
    # Information about the GUI properties can be read on the get_piece_position function.
    horizontal_distance = square_dist * 2
    vertical_distance = square_dist
    row = coords[0]
    column = coords[1]
    
    x_pos = top_left_coords[0] + (horizontal_distance * (column // 2))
    x_pos = x_pos if row % 2 == 0 else x_pos + vertical_distance
    y_pos = top_left_coords[1] + (vertical_distance * row)
    
    return (x_pos, y_pos)