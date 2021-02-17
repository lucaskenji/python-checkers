import sys
sys.path.append('..')
from piece import Piece

def test_piece_getters():
    test_piece = Piece('16WN')
    assert test_piece.get_position() == '16'
    assert test_piece.get_color() == 'W'
    assert test_piece.is_king() == False