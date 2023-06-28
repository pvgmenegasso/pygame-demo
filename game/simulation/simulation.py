from dataclasses import dataclass, field
from enum import Enum
from typing import NamedTuple
from pygame.time import Clock

from game.entities.player import Player
from game.simulation.constants import Difficulty
from game.simulation.resources import Resources


class Speed(Enum):
    fastest = 4
    fast = 2
    normal = 1
    stop = 0


@dataclass
class Simulation:
    players: list[Player] = field(default_factory=dict)
    speed: Speed = field(default=Speed.normal)
    _steps: int = 0

    def update(self, difficulty: Difficulty):
        self._steps += self.speed
        for player in self.players:
            player.update(difficulty=difficulty, speed=self.speed)

    def get_time_s(self, fps: int) -> float:
        return self._steps / fps
