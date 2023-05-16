from __future__ import annotations
from typing import Any, ClassVar
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
    def __init__(self, groups: Any, file_arg: str = "my_image.jpg")-> None:
        super().__init__(groups)
        self.image = load_extended(file_arg)
        self.rect = self.image.get_rect()
        self.rect.center = (
            randint(horizontal_bounds.x.__ceil__(), horizontal_bounds.y.__ceil__()),
            randint(vertical_bounds.x.__ceil__(), vertical_bounds.y.__ceil__()),
        )


    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, self.rect)


class MySprite(SpriteLoader):
    surface: ClassVar[Surface] = DISPLAY

    def __init__(self)-> None:
        with open("assets/my_image.jpg") as file:
            super().__init__(file.read())

    def update(self)-> None:
        SpriteLoader.update

    @override
    def draw(
        self,
        surface: Surface | None = None
    )-> Any:
        if surface is None:
            surface = MySprite.surface
        surface.blit(self.image, self.rect)
