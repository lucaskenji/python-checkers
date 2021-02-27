import pygame as pg
from sys import exit
from pygame.locals import *
from board_gui import BoardGUI

def main():
    pg.init()
    FPS = 30
    
    DISPLAYSURF = pg.display.set_mode((700, 500))
    pg.display.set_caption('Checkers in Python')
    fps_clock = pg.time.Clock()

    board_gui = BoardGUI((26, 26))

    while True:
        DISPLAYSURF.fill((0, 0, 0))
        board_gui.draw_board(DISPLAYSURF)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return
        
        pg.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
    exit()