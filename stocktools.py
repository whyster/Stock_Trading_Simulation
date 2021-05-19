import random
from typing import NamedTuple


class Properties(NamedTuple):
    min_rate: int
    max_rate: int
    max_steps: int


class TrendGenerator:
    def __init__(self, properties: Properties):
        self.prop = properties
        self.grow_steps = 0
        self.grow_rate = 0
        self.value = 0

    def __iter__(self):
        self.grow_steps = 0
        self.grow_rate = 0
        self.value = 0
        return self

    def __next__(self):
        if self.grow_steps != 0:
            sign = self.grow_steps.__abs__() / self.grow_steps
            self.grow_steps -= sign
            self.value += self.grow_rate * sign
        elif self.grow_steps == 0:
            self.grow_rate = random.randint(self.prop.min_rate, self.prop.max_rate)
            self.grow_steps = random.randint(-self.prop.max_steps, self.prop.max_steps)

        return self.value




