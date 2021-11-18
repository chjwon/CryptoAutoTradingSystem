import pyupbit


def VBS(ticker, k): # Volatility Breakthrough Strategy 
    """Breakthrough volatility strategy to view buying targets"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price