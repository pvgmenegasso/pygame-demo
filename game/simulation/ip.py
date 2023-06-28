from __future__ import annotations
from dataclasses import dataclass
from random import random
from typing import ClassVar
from game.simulation.constants import Difficulty
from datetime import date
from dateutil.relativedelta import relativedelta


@dataclass
class IP:
    accumulated_costs: ClassVar[int] = 0
    value: float = 0
    release_date: date | None = None
    monthly_value: float = 0
    _completion: int = 0
    completion_cost: int

    @classmethod
    def gen_ip() -> IP:
        completion_cost: int = round(random() * min(IP.accumulated_costs, 100))
        IP.accumulated_costs += completion_cost
        return IP(completion_cost=completion_cost)

    def is_complete(self) -> bool:
        if self._completion >= self.completion_cost:
            return True
        return False

    def complete(self, commited_progress: int) -> int:
        """
        Returns
        -------
        int:
            Unused of progress value
        """
        if not self.is_complete():
            points_to_completion = self.completion_cost - self._completion
            if points_to_completion > commited_progress:
                self._completion += commited_progress
                return 0
            else:
                self._completion = self.completion_cost
                return commited_progress - points_to_completion
        return commited_progress

    def time_passed(self, current_date: date) -> relativedelta:
        return relativedelta(current_date, self.release_date)

    def monthly_decrease(self, difficulty: Difficulty) -> float:
        return self.value * difficulty.ip_monthly_value_decrease_rate

    def calculate_value_in_n_months(self, n: int, difficulty: Difficulty) -> float:
        value = self.value
        while range(n):
            self.value -= self.monthly_decrease(difficulty=difficulty)

        return_value = self.value

        # reset to starting value
        self.value = value

        return return_value

    def calculate_current_value(
        self, difficulty: Difficulty, current_date: date
    ) -> float:
        return self.calculate_value_in_n_months(
            n=self.time_passed(current_date=current_date).months, difficulty=difficulty
        )

    def update_monthly_value(self, difficulty: Difficulty) -> None:
        self.monthly_value -= (
            self.monthly_value * difficulty.ip_monthly_value_decrease_rate
        )
