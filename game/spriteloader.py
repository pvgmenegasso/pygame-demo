from __future__ import annotations
from typing import ClassVar
from typing_extensions import override

from pygame import Vector2

from constants import DISPLAY, SCREEN_HEIGHT, AnyPath, SCREEN_WIDTH
from pygame.sprite import Sprite
from pygame.image import load_extended
from pygame.surface import Surface
from random import randint


horizontal_bounds = Vector2(0, SCREEN_WIDTH)
vertical_bounds = Vector2(0, SCREEN_HEIGHT)


class SpriteLoader(Sprite):
    surface: ClassVar[Surface] = DISPLAY

    def __init__(self, file_arg: str = "my_image.jpg") -> None:
        super().__init__()
        self.image = load_extended(file_arg)
        self.rect = self.image.get_rect()
        self.rect.center = (
            randint(horizontal_bounds.x, horizontal_bounds.y),
            randint(vertical_bounds.x, vertical_bounds.y),
        )

    @property
    def update(self):
        pass

    def draw(self, surface: Surface):
        surface.blit(self.image, self.rect)


class MySprite(SpriteLoader):
    def __init__(self) -> None:
        super().__init__(file_arg="assets/my_image.jpg")

    def update(self):
        return super().update

    @override
    def draw(self):
        MySprite.surface.blit(self.image, self.rect)
