from dataclasses import dataclass, field
from entities.player import Player
from simulation.constants import Difficulty
from simulation.simulation import Simulation, Speed


@dataclass
class Scene:
    _simulation: Simulation | None = None
    _speed: Speed = Speed.stop
    _players: list[Player] = field(default_factory=list)

    def __post_init__(self):
        self._simulation = Simulation(
            players=self._players,
            speed=self._speed,
        )

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def set_speed(self, speed: Speed):
        self._speed = speed

    def update(self, difficulty: Difficulty) -> None:
        self._simulation.update(difficulty=difficulty)

    def print_stats(self) -> None:
        for player in self._simulation.players:
            print(player.name)
            for employee in player.employees:
                print(employee)
            print(player.resources)
