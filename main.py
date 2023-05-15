import sys
from typing import NoReturn
import pygame.event
import pygame.display
import pygame as pg
from game.constants import DISPLAY, MainThene, TITLE, ICONTITLE, FPS


# init pygame first !


from pygame.time import Clock
from game.spriteloader import MySprite


def spawn_sprite():
    MySprite.surface = DISPLAY
    return MySprite()


def safe_init():
    pg.init()
    DISPLAY.fill(MainThene.BLACK)
    pygame.display.set_caption(TITLE, ICONTITLE)


def safe_quit() -> NoReturn:
    quit()
    sys.exit()


def game_loop():
    # Game loop
    while True:
        # code
        # Read event queue
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                safe_quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                safe_quit()
        MySprite().draw()
        pygame.display.update()
        Clock().tick(FPS)


# Check collision between to rects
# object1 = pygame.Rect((20, 50), (50, 100))
# object2 = pygame.Rect((10, 10), (100, 100))

# print(object1.colliderect(object2))

# We can also check for a collision between a Rect and a pair of coordinates.
# object1 = pygame.Rect((20, 50), (50, 100))
#
# print(object1.collidepoint(50, 75))
