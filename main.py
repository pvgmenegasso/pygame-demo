import sys
from typing import NoReturn
from pygame.event import get
from pygame import MOUSEBUTTONDOWN
from pygame import init, QUIT, quit
from pygame.display import set_caption, update

# init pygame first !
init()

from constants import DISPLAY, MainThene, TITLE, ICONTITLE, FPS
DISPLAY.fill(MainThene.BLACK)
set_caption(TITLE, ICONTITLE)
from pygame.time import Clock
from spriteloader import MySprite
MySprite.surface = DISPLAY

sprite = MySprite()

def safe_quit() -> NoReturn:
    quit()
    sys.exit()

# Game loop
while True:
    # code
    # Read event queue
    for event in get():
        if event.type == QUIT:
            safe_quit()
        if event.type == MOUSEBUTTONDOWN:
            safe_quit()
    MySprite().draw()
    update()
    Clock().tick(FPS)




# Check collision between to rects
# object1 = pygame.Rect((20, 50), (50, 100))
# object2 = pygame.Rect((10, 10), (100, 100))
 
# print(object1.colliderect(object2))

# We can also check for a collision between a Rect and a pair of coordinates.
# object1 = pygame.Rect((20, 50), (50, 100))
#  
# print(object1.collidepoint(50, 75))