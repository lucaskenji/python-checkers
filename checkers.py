import pygame as pg
from sys import exit
from pygame.locals import *
from board_gui import BoardGUI
from game_control import GameControl

def main():
    pg.init()
    FPS = 30
    
    DISPLAYSURF = pg.display.set_mode((700, 500))
    pg.display.set_caption('Checkers in Python')
    fps_clock = pg.time.Clock()

    game_control = GameControl("W")

    main_font = pg.font.SysFont("Arial", 25)
    turn_rect = (509, 26)
    winner_rect = (509, 152)

    while True:
        DISPLAYSURF.fill((0, 0, 0))
        game_control.draw_screen(DISPLAYSURF)

        turn_display_text = "White's turn" if game_control.get_turn() == "W" else "Black's turn"
        DISPLAYSURF.blit(main_font.render(turn_display_text, True, (255, 255, 255)), turn_rect)

        if game_control.get_winner() is not None:
            winner_display_text = "White wins!" if game_control.get_winner() == "W" else "Black wins!"
            DISPLAYSURF.blit(main_font.render(winner_display_text, True, (255, 255, 255)), winner_rect)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return
            
            if event.type == MOUSEBUTTONDOWN:
                game_control.hold_piece(event.pos)
            
            if event.type == MOUSEBUTTONUP:
                game_control.release_piece()
        
        pg.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
    exit()