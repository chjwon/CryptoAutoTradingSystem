import time
import pyupbit
import datetime
import VBS_model as md
from Slack import post_message

accessTXT = open('access.txt','r')
access = accessTXT.read()
# accessTXT.close()

secretTXT = open('secret.txt','r')
secret = secretTXT.read()
# secretTXT.close()

myTokenTXT = open('myToken.txt','r')
myToken = myTokenTXT.read()
# myTokenTXT.close()


# Get the aiming price
def get_target_price(ticker, k):
    target_price = md.VBS(ticker,k)
    return target_price

def get_start_time(ticker):
    """get start time"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1) # 9h
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15-Day Moving Average Line"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(coin):
    """Check balance"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """Current price check"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# login
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# send start messaage to Slack
post_message(myToken,"#autotrading", "autotrading start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC") # 9am
        end_time = start_time + datetime.timedelta(days=1) # 9am +1D
        print(now)

        # Set a buyout target for 9 to 8:59:50 seconds the next day.
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                # post_message(myToken,"#autoTrading","KRW balance: "+str(krw))
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    post_message(myToken,"#autotrading", "BTC buy : " +str(buy_result))
        else:
            btc = get_balance("BTC")
            # post_message(myToken,"#autoTrading","BTC balance: "+str(btc))
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#autotrading", "BTC sell : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        # print(e)
        # post_message(myToken,"#autotrading", e)
        # time.sleep(1)
        pass