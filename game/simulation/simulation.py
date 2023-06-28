from dataclasses import dataclass, field
from entities.player import Player
from simulation.speed import Speed
from simulation.constants import Difficulty


@dataclass
class Simulation:
    players: list[Player] = field(default_factory=list)
    speed: Speed = field(default=Speed.normal)
    _steps: int = 0

    def update(self, difficulty: Difficulty):
        self._steps += self.speed
        for player in self.players:
            player.update(difficulty=difficulty, speed=self.speed)

    def get_time_s(self, fps: int) -> float:
        return self._steps / fps
