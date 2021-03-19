from board import Board
from piece import Piece
from held_piece import HeldPiece
from utils import get_piece_gui_coords, get_surface_mouse_offset, get_piece_position
import pygame

BLACK_PIECE_SURFACE = pygame.image.load("images/black_piece.png")
WHITE_PIECE_SURFACE = pygame.image.load("images/white_piece.png")
BLACK_KING_PIECE_SURFACE = pygame.image.load("images/black_king_piece.png")
WHITE_KING_PIECE_SURFACE = pygame.image.load("images/white_king_piece.png")
BOARD = pygame.image.load("images/board.png")
TOPLEFTBORDER = (34, 34)
SQUARE_DIST = 56

class BoardGUI:
    def __init__(self, board_rect):
        # Initial setup
        pieces = []

        for opponent_piece in range(0, 12):
            pieces.append(Piece(str(opponent_piece) + 'BN'))
        
        for player_piece in range(20, 32):
            pieces.append(Piece(str(player_piece) + 'WN'))

        # Attributes
        self.board = Board(pieces, "W")
        self.piece_rects = self.get_piece_rects(pieces)
        self.piece_colors = self.get_piece_colors(pieces)
        self.piece_status = self.get_piece_status(pieces)
        self.board_rect = board_rect
        self.held_piece = None
        self.held_piece_index = -1
        self.move_marks = []

    def get_piece_rects(self, pieces):
        # Receives a list of Piece instances, returns a list of appropriate positions on the board as a tuple (x, y)
        rects = []

        for piece in pieces:
            pos = int(piece.get_position())
            row = self.board.get_row_number(pos)
            column = self.board.get_col_number(pos)
            
            # Calculates where the piece should be based on row and column positions
            rects.append(pygame.Rect(get_piece_gui_coords((row, column), SQUARE_DIST, TOPLEFTBORDER), (41, 41)))
        
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

    def draw_gui(self, display_surface):
        # Draws the board along with its pieces and any piece being held with the mouse.
        self.draw_board(display_surface)
        
        image_rect = pygame.image.load("images/marking.png")

        if self.held_piece is not None:
            for move_mark in self.move_marks:
                display_surface.blit(image_rect, move_mark)

            self.held_piece.draw_piece(display_surface)

    def draw_board(self, display_surface):
        # Draws a board and its pieces on the display surface.
        display_surface.blit(BOARD, self.board_rect)

        for index, piece_rect in enumerate(self.piece_rects):
            if self.held_piece is not None:
                if index == self.held_piece_index:
                    continue

            if self.piece_status[index]:
                display_surface.blit(BLACK_KING_PIECE_SURFACE if self.piece_colors[index] == "B" else WHITE_KING_PIECE_SURFACE, piece_rect)
            else:
                display_surface.blit(BLACK_PIECE_SURFACE if self.piece_colors[index] == "B" else WHITE_PIECE_SURFACE, piece_rect)
    
    def hold_piece_with_mouse(self, mouse_pos):
        # If a piece is clicked in the given mouse position, makes a piece follow the mouse and hides it from the board.
        piece_clicked = self.get_piece_on_mouse(mouse_pos)

        if piece_clicked is not None:
            forced_to_eat = False

            # Checks if a piece of the color of the piece clicked has a move that eats an opponent piece.
            # If it does, allow only moves to eat pieces.
            for piece in self.board.get_pieces():
                for move in piece.get_moves(self.board):
                    if move["eats_piece"]:
                        if piece.get_color() == piece_clicked.get_color():
                            forced_to_eat = True
                            break
                else:
                    continue
                break
            
            piece_moves = piece_clicked.get_moves(self.board)

            if forced_to_eat:
                piece_moves = list(filter(lambda move: move["eats_piece"] == True, piece_moves))

            for possible_move in piece_moves:
                row = self.board.get_row_number(int(possible_move["position"]))
                column = self.board.get_col_number(int(possible_move["position"]))
                self.move_marks.append(pygame.Rect(get_piece_gui_coords((row, column), SQUARE_DIST, TOPLEFTBORDER), (44, 44)))

            self.set_held_piece(int(piece_clicked.get_position()), mouse_pos)
    
    def release_piece(self):
        # If a piece is released, tell the board to execute the move, remove all marks and stop holding the piece.
        if self.held_piece is not None:
            released_on = self.held_piece.check_collision(self.move_marks)

            if released_on is not None:
                self.board.move_piece(self.held_piece_index, get_piece_position((released_on.x, released_on.y), SQUARE_DIST, TOPLEFTBORDER))
                self.update_board()
            
            self.set_held_piece(-1, None)
            self.move_marks = []

    def get_piece_on_mouse(self, mouse_pos):
        # Given a tuple with the mouse's x and y position, returns the piece clicked or None if no piece was clicked.
        piece_index = -1

        for index, piece_rect in enumerate(self.piece_rects):
            if piece_rect.collidepoint(mouse_pos):
                piece_index = index
                break
        else:
            return None
        
        return self.board.get_piece_by_index(piece_index)
    
    def set_held_piece(self, position, mouse_pos):
        # Given a piece's position as an integer, finds the piece object and sets held_piece and held_piece_index.
        # Sets held_piece to None if -1 is given as a position.
        if position == -1:
            self.held_piece = None
            self.held_piece_index = -1
            return

        piece_row = self.board.get_row_number(position)
        piece_column = self.board.get_col_number(position)

        piece_rect = pygame.Rect(get_piece_gui_coords((piece_row, piece_column), SQUARE_DIST, TOPLEFTBORDER), (41, 41))

        for index, rect in enumerate(self.piece_rects):
            if rect.colliderect(piece_rect):
                piece_to_hold = self.board.get_piece_by_index(index)
                offset = get_surface_mouse_offset(piece_rect, mouse_pos)
                self.held_piece = HeldPiece(self.get_piece_surface(piece_to_hold.get_color(), piece_to_hold.is_king()), offset)
                self.held_piece_index = index
    
    def get_piece_surface(self, color, is_king):
        # Given color and king properties, returns an appropriate surface.
        piece_surfaces = [BLACK_KING_PIECE_SURFACE, WHITE_KING_PIECE_SURFACE] if is_king else [BLACK_PIECE_SURFACE, WHITE_PIECE_SURFACE]

        if color == "B":
            return piece_surfaces[0]
        else:
            return piece_surfaces[1]
    
    def update_board(self):
        pieces = self.board.get_pieces()
        self.piece_rects = self.get_piece_rects(pieces)
        self.piece_colors = self.get_piece_colors(pieces)
        self.piece_status = self.get_piece_status(pieces)