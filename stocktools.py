import random
from typing import NamedTuple, Union
from tradetools import *


class Properties(NamedTuple):
    min_rate: Union[int, float]
    max_rate: Union[int, float]
    max_steps: int


class TrendGenerator:
    def __init__(self, properties: Properties):
        self.prop = properties
        self.grow_steps = 0
        self.grow_rate = 0
        self.value = 0
        # self.random = random.Random()

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

            self.grow_rate = random.uniform(self.prop.min_rate, self.prop.max_rate)
            self.grow_steps = random.randint(-self.prop.max_steps, self.prop.max_steps)

        return self.value


class BasicDemand(TrendGenerator):
    def __init__(self, properties: Properties, stock_name, stock_count: int):
        super().__init__(properties)
        self.current_stock: int = stock_count
        self.max_stock: int = self.current_stock
        self.name = stock_name
        self.trade_flag = False

    def __next__(self):
        self.value = super().__next__()
        demand = 0
        if self.current_stock == 0:
            demand = self.max_stock
        else:
            demand = (self.max_stock / self.current_stock) - 1
        self.value += demand

        self.trade_flag = True
        return self.value

    def purchase(self, amount, stock_account: StockAccount):
        if not self.trade_flag:
            raise PermissionError("Only 1 trade per cycle")

        if self.current_stock < amount:
            raise ValueError("Not enough company stock to sell")

        self.current_stock -= amount
        stock_account.money_to_stock(stock_name=self.name, stock_amount=amount, value=self.value)
        self.trade_flag = False

    def sell(self, amount, stock_account: StockAccount):
        if not self.trade_flag:
            raise PermissionError("Only 1 trade per cycle")

        self.current_stock += amount
        stock_account.stock_to_money(stock_name=self.name, stock_amount=amount, value=self.value)
        self.trade_flag = False
