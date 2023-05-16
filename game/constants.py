# This helps separating namespace from polluted names that pygame uses in it's examples.
# Also we define here some magic custom types which are not exported by pygame, so AnyPath and FileArg types had to be defined
# by ctrl+c ctrl+v to avoid importing protected namespace

from typing import LiteralString, TypeAlias
from pygame.color import Color
from pygame import Vector2
from pygame.display import set_mode
from pygame.time import Clock
from os import PathLike
from typing import IO, final

SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1600
SCREEN_SIZE = Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

TITLE: LiteralString = "TEST GAME"
ICONTITLE: LiteralString = "TEST GAME ICONTITLE"
AnyPath: TypeAlias = str | bytes


class Transparency:
    __lowest_transparency = 1
    __max_transparency = 255

    @classmethod
    def n_transparent(cls, fraction: int) -> int:
        result = int(255 / fraction)
        if result < cls.__lowest_transparency or result > cls.__max_transparency:
            raise ValueError(
                f"Your fraction would result in an Alpha {result}. which is greater than {cls.__max_transparency} or smaller than {cls.__lowest_transparency}. You did something wrong"
            )
        return int(255 / fraction)


class MainThene:
    COLOR_BG = Color(20, 0, 20)
    COLOR_FG = Color(255, 255, 255)
    COLOR_ACCENT = Color(120, 30, 255)
    COLOR_TEXT = Color(255, 255, 255)
    COLOR_PANELS = Color(80, 20, 255)
    BLACK = Color(0, 0, 0)
    WHITE = Color(255, 255, 255)
    GREY = Color(128, 128, 128)


DISPLAY = set_mode(SCREEN_SIZE)
