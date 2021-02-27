from board import Board
from piece import Piece
import pygame

BLACK_PIECE_SURFACE = pygame.image.load("images/black_piece.png")
WHITE_PIECE_SURFACE = pygame.image.load("images/white_piece.png")

class BoardGUI:
    def __init__(self):
        # Initial setup
        pieces = []

        for opponent_piece in range(1, 8):
            pieces.append(Piece(str(opponent_piece) + 'BN'))
        
        for player_piece in range(24, 31):
            pieces.append(Piece(str(player_piece) + 'WN'))

        # Attributes
        self.board = Board(pieces, "W")
        self.piece_rects = get_piece_rects(pieces)
        self.piece_colors = get_piece_colors(pieces)
        self.piece_status = get_piece_status(pieces)

    def get_piece_rects(self, pieces):
        TOPLEFTBORDER = (35, 35)
        rects = []

        for piece in pieces:
            pos = int(piece.get_position())
            row = self.board.get_row_number(pos)
            column = self.board.get_col_number(pos)
            
            x_pos = TOPLEFTBORDER[0] + (113 * (column // 2))
            x_pos = x_pos if row % 2 == 0 else x_pos + 57
            y_pos = TOPLEFTBORDER[1] + (57 * row)

            rects.append((x_pos, y_pos))
        
        return rects
    
    def get_piece_colors(self, pieces):
        colors = []

        for piece in pieces:
            colors.append(piece.get_color())
        
        return colors
    
    def get_piece_status(self, pieces):
        status = []

        for piece in pieces:
            status.append(piece.is_king())
        
        return status

    def draw_board(self, display_surface):
        for index, piece_rect in self.piece_rects:
            display_surface.blit(BLACK_PIECE_SURFACE if piece_colors[index] == "B" else WHITE_PIECE_SURFACE, piece_rect)