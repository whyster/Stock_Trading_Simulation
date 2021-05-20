from collections import defaultdict

class StockAccount:
    def __init__(self, starting_income: int, starting_stocks: defaultdict[str, int] = None):
        self.money = starting_income
        if starting_stocks:
            self.stocks = starting_stocks
        else:
            self.stocks = defaultdict(int)

    def stock_to_money(self, stock_name, stock_amount, value):
        stock_count = self.stocks.get(stock_name, 0)

        if stock_count < stock_amount:
            raise ValueError("Not enough stocks to sell")

        stock_count -= stock_amount
        self.stocks[stock_name] = stock_count
        self.money += value * stock_amount

    def money_to_stock(self, stock_name, stock_amount, value):

        if self.money < value * stock_amount:
            raise ValueError("Not enough money to buy stocks")

        if value < 0:
            value = 1
        self.money -= value * stock_amount
        stock_count = self.stocks.get(stock_name, 0)
        self.stocks[stock_name] = stock_count + stock_amount

