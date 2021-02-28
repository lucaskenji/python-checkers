def get_piece_position(coords, gui_properties):
    # Receives a piece's x and y coordinates along with the GUI's specific properties, returning a piece's position (0 - 31) on the board.
    # GUI properties should be a list containing two tuples, one with the horizontal and vertical distance of each piece, and other
    # with the top left corner's coordinates.
    horizontal_distance = gui_properties[0][0]
    vertical_distance = gui_properties[0][1]
    top_left_coords = gui_properties[1]
    pass

def get_piece_gui_coords(coords, gui_properties):
    # Receives a piece's row and column position along with the GUI's specific properties, returning a piece's coordinates on the GUI.
    # Information about the GUI properties can be read on the get_piece_position function.
    horizontal_distance = gui_properties[0][0]
    vertical_distance = gui_properties[0][1]
    top_left_coords = gui_properties[1]
    row = coords[0]
    column = coords[1]
    
    x_pos = top_left_coords[0] + (horizontal_distance * (column // 2))
    x_pos = x_pos if row % 2 == 0 else x_pos + vertical_distance
    y_pos = top_left_coords[1] + (vertical_distance * row)
    
    return (x_pos, y_pos)