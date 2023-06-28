import sys
from typing import NoReturn
import pygame.event
import pygame.display
import pygame as pg
from constants import DISPLAY, MainThene, TITLE, ICONTITLE, FPS


# init pygame first !


from pygame.time import Clock
from entities.employee import Employee, Skills, Stats
from entities.player import Player
from scenes.scene_0 import Scene
from simulation.constants import Difficulty
from simulation.ip import IP
from simulation.resources import Resources
from simulation.simulation import Simulation, Speed
from spriteloader import MySprite


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


sprite = spawn_sprite()
spirtes = pg.sprite.Group(sprite)
clock = Clock()
player = Player(
    name="test_player",
    employees=[Employee(stats=Stats(), skills=Skills.gen_skills())],
    resources=Resources(ips=[IP.gen_ip()]),
)

scene = Scene()
scene.add_player(player)
scene.set_speed(speed=Speed.fast)


def game_loop() -> NoReturn:
    # Game loop
    while True:
        scene.update(difficulty=Difficulty(ip_monthly_value_decrease_rate=0.03))
        scene.print_stats()
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


game_loop()

# Check collision between to rects
# object1 = pygame.Rect((20, 50), (50, 100))
# object2 = pygame.Rect((10, 10), (100, 100))

# print(object1.colliderect(object2))

# We can also check for a collision between a Rect and a pair of coordinates.
# object1 = pygame.Rect((20, 50), (50, 100))
#
# print(object1.collidepoint(50, 75))
