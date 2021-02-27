from board import Board
from piece import Piece
import pygame

BLACK_PIECE_SURFACE = pygame.image.load("images/black_piece.png")
WHITE_PIECE_SURFACE = pygame.image.load("images/white_piece.png")
BOARD = pygame.image.load("images/board.png")

class BoardGUI:
    def __init__(self, board_rect):
        # Initial setup
        pieces = []

        for opponent_piece in range(0, 8):
            pieces.append(Piece(str(opponent_piece) + 'BN'))
        
        for player_piece in range(24, 32):
            pieces.append(Piece(str(player_piece) + 'WN'))

        # Attributes
        self.board = Board(pieces, "W")
        self.piece_rects = self.get_piece_rects(pieces)
        self.piece_colors = self.get_piece_colors(pieces)
        self.piece_status = self.get_piece_status(pieces)
        self.board_rect = board_rect

    def get_piece_rects(self, pieces):
        # Receives a list of Piece instances, returns a list of appropriate positions on the board as a tuple (x, y)
        TOPLEFTBORDER = (34, 34)
        HORIZONTAL_DIST = 112
        VERTICAL_DIST = 56
        rects = []

        for piece in pieces:
            pos = int(piece.get_position())
            row = self.board.get_row_number(pos)
            column = self.board.get_col_number(pos)
            
            # Calculates where the piece should be based on row and column positions
            x_pos = TOPLEFTBORDER[0] + (HORIZONTAL_DIST * (column // 2))
            x_pos = x_pos if row % 2 == 0 else x_pos + VERTICAL_DIST
            y_pos = TOPLEFTBORDER[1] + (VERTICAL_DIST * row)

            rects.append((x_pos, y_pos))
        
        return rects
    
    def get_piece_colors(self, pieces):
        # Receives a list of Piece instances, returns the color of the piece. Used to render proper colored pieces on the board.
        colors = []

        for piece in pieces:
            colors.append(piece.get_color())
        
        return colors
    
    def get_piece_status(self, pieces):
        # Receives a list of Piece instances, returns if the piece is a king. Used to render kings on the board.
        status = []

        for piece in pieces:
            status.append(piece.is_king())
        
        return status

    def draw_board(self, display_surface):
        # Draws a board and its pieces on the display surface.
        display_surface.blit(BOARD, self.board_rect)

        for index, piece_rect in enumerate(self.piece_rects):
            display_surface.blit(BLACK_PIECE_SURFACE if self.piece_colors[index] == "B" else WHITE_PIECE_SURFACE, piece_rect)