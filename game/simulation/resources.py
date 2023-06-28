from dataclasses import dataclass, field

from game.simulation.ip import IP


@dataclass
class Resources:
    cash: float = 0
    max_manpower: int = 10
    ips: list[IP] = field(default_factory=list)
