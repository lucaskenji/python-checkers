import pygame as pg
from sys import exit
from pygame.locals import *

def main():
    pg.init()
    FPS = 30
    
    DISPLAYSURF = pg.display.set_mode((700, 500))
    pg.display.set_caption('Checkers in Python')
    fps_clock = pg.time.Clock()

    BOARD_BG = pg.image.load('images/board.png')
    BOARD_RECT = (26, 26)

    while True:
        DISPLAYSURF.blit(BOARD_BG, BOARD_RECT)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return
        
        pg.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
    exit()