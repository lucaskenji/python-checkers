from pygame.mouse import get_pos as get_mouse_pos

class HeldPiece:
    def __init__(self, surface, offset):
        self.surface = surface
        self.offset = offset

    def draw_piece(self, display_surface):
        mouse_pos = get_mouse_pos()
        draw_rect = (mouse_pos[0] + self.offset[0], mouse_pos[1] + self.offset[1])

        display_surface.blit(self.surface, draw_rect)