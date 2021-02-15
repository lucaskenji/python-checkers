import sys
sys.path.append('..')
import board

def test_has_piece():
    test_board = Board(['12WY', '26BY', '8WN'])
    assert test_board.has_piece(26) == True
    assert test_board.has_piece(10) == False

def test_get_row_number():
    test_board = Board([])
    assert Board.get_row_number(3) == 0
    assert Board.get_row_number(4) == 0
    assert Board.get_row_number(5) == 1