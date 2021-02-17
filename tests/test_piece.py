import sys
sys.path.append('..')
from piece import Piece

def test_piece_getters():
    test_piece = Piece('16WN')
    assert test_piece.getPosition() == '16'
    assert test_piece.getColor() == 'W'
    assert test_piece.isKing() == False