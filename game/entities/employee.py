from __future__ import annotations
from dataclasses import dataclass
from random import randint
from simulation.ip import IP

from simulation.speed import Speed


@dataclass
class Skills:
    """
    attributes
    ----------
    techical_skill: int
        0-10 value representing one's skill
    charisma: int
        0-10 value representing one's charisma
    """

    techical_skill: int
    charisma: int

    @classmethod
    def gen_skills(cls) -> Skills:
        return Skills(techical_skill=randint(1, 10), charisma=randint(1, 10))


@dataclass
class Stats:
    """
    attributes
    ----------
    happyness: int
        0-100
    lazyness: int
        0-100
    """

    happyness: int = 100
    lazyness: int = 100

    def get_productivity(self, skills: Skills) -> float:
        """
        0-100 value representing how much one is currently productive
        """
        lazyness_rate: float = self.lazyness / 100 if self.lazyness > 0 else 0
        happyness_rate: float = self.happyness / 100 if self.happyness > 0 else 0

        return max(
            (happyness_rate + 1)
            * (skills.charisma * skills.techical_skill)
            * (1 - lazyness_rate),
            100,
        )


@dataclass
class Employee:
    stats: Stats
    skills: Skills

    def update_stats(self, speed: Speed) -> None:
        self.stats.happyness -= speed
        self.stats.lazyness += speed

    def work(self, speed: Speed, ips: list[IP]) -> None:
        self.update_stats(speed=speed)

        production_capacity = self.stats.get_productivity(self.skills) * speed

        for ip in ips:
            production_capacity = ip.complete(commited_progress=production_capacity)
            if production_capacity == 0:
                return
