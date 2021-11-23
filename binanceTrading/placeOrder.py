import ccxt

binance = ccxt.binance()


def orderMarketPrice(coinTicker, buy_sell, amount):
    if buy_sell == "buy":
        order = binance.create_limit_buy_order(coinTicker, amount)
    elif but_sell == "sell":
        order = binance.create_limit_sell_order(coinTicker, amount)
    else:
        pass
    return str(order)


def orderLimitPrice(coinTicker, buy_sell, amount, price):
    if buy_sell == "buy":
        order = binance.create_limit_buy_order(coinTicker, amount, price)
    elif but_sell == "sell":
        order = binance.create_limit_sell_order(coinTicker, amount, price)
    else:
        pass
    return str(order)
