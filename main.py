from stocktools import *
from tradetools import StockAccount





def simple_trade_account():
    generic_demand: BasicDemand = BasicDemand(Properties(min_rate= 1.0, max_rate=2.0, max_steps=3), "GENERIC", 10000)
    stock_account: StockAccount = StockAccount(100)
    file_handle = open("test_graphs/basic_test.csv", 'w')
    print('starting sim')
    for _ in range(10**7):

        cost = next(generic_demand)
        # print(f"{_}:\t{generic_demand.value}\t{stock_account.money}\t{stock_account.stocks[generic_demand.name]}")

        if stock_account.money/2 > cost and stock_account.money > 1:
            generic_demand.purchase(1, stock_account)
        elif stock_account.money < cost/2:
            try:
                generic_demand.sell(1, stock_account)
            except Exception as e:
                print(e)
        file_handle.write(f"{generic_demand.value}\t{stock_account.money}\t{stock_account.stocks[generic_demand.name]}\n")



# def argparse():
    # return None

def main():
    simple_trade_account()

if __name__ == '__main__':
    # args = argparse()
    main()


