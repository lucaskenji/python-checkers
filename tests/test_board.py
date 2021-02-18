import sys
sys.path.append('..')
from board import Board
from piece import Piece

def test_has_piece():
    # Simple test to assert has_piece detects a piece on a given position.
    test_board = Board([Piece('12WY'), Piece('26BY'), Piece('8WN')], 'W')
    assert test_board.has_piece(26) == True
    assert test_board.has_piece(10) == False

def test_get_row_number():
    # Asserts if get_row_number correctly returns the row for a given position. The first row is 0.
    # Positions are also zero-indexed.
    test_board = Board([], 'W')
    assert test_board.get_row_number(2) == 0
    assert test_board.get_row_number(3) == 0
    assert test_board.get_row_number(4) == 1

def test_get_col_number():
    # Asserts if get_col_number correctly returns the column for a given position. The first column is 0.
    test_board = Board([], 'B')
    assert test_board.get_col_number(0) == 0
    assert test_board.get_col_number(1) == 2
    assert test_board.get_col_number(4) == 1
    assert test_board.get_col_number(31) == 7