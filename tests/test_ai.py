import sys
sys.path.append('..')
from piece import Piece
from board import Board
from ai import AI

def test_minimax_maximize():
    # minimax() returns the maximum value possible
    test_ai = AI('B')
    test_board = Board([Piece('9WN'), Piece('13BN')], 'B')
    assert test_ai.minimax(test_board, True, 1, 'B') == 1

def test_minimax_minimize():
    # minimax() returns the minimum value possible
    test_ai = AI('B')
    test_board = Board([Piece('9WN'), Piece('13BN')], 'B')
    assert test_ai.minimax(test_board, False, 1, 'B') == 0

def test_get_move():
    # get_move() should return the move with the maximum value
    test_ai = AI('B')
    test_board = Board([Piece('9WN'), Piece('13BN')], 'B')
    assert test_ai.get_move(test_board) == {"position": "4", "eats_piece": True}