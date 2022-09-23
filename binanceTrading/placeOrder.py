import ccxt

binance = ccxt.binance()


def orderMarketPrice(coinTicker, position, amount):
    if position == "buy":
        order = binance.create_limit_buy_order(coinTicker, amount)
    elif position == "sell":
        order = binance.create_limit_sell_order(coinTicker, amount)
    else:
        pass
    return str(order)


def orderLimitPrice(coinTicker, position, amount, price):
    if position == "buy":
        order = binance.create_limit_buy_order(coinTicker, amount, price)
    elif position == "sell":
        order = binance.create_limit_sell_order(coinTicker, amount, price)
    else:
        pass
    return str(order)
