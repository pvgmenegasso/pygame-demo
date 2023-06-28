from dataclasses import dataclass
from game.entities.employee import Employee
from game.simulation.constants import Difficulty
from game.simulation.resources import Resources
from game.simulation.simulation import Speed


@dataclass
class Player:
    resources: Resources
    employees: list[Employee]

    def __post_init__(self):
        if len(self.employees) > self.resources.max_manpower:
            raise RuntimeError(
                f"Cannot have more employees than {self.resources.max_manpower}"
            )

    def update(self, difficulty: Difficulty, speed: Speed) -> None:
        if speed != Speed.stop:
            for employee in self.employees:
                employee.work(speed=speed, ips=self.resources.ips)

            # Only receive for completed ips
            for ip in filter(lambda x: x.is_complete(), self.resources.ips):
                for _ in range(speed):
                    ip.update_monthly_value(difficulty=difficulty)
                    self.resources.cash += ip.monthly_value()
