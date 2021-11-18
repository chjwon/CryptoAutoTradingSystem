from os import write
from re import template
import ccxt
from datetime import date, datetime
import csv



"""
WIP
ohlcvs
Date / Start / High / Low / End / Volume
"""

binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('BTC/USDT')

for ohlc in ohlcvs:
    ohlc[0] = datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S')

print(ohlcvs[-3])
print(ohlcvs[-2])
print(ohlcvs[-1])

category = ["Date", "Start", "High", "Low", "End", "Volume"]
with open('BTC_Price.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(category)
    for i in range(len(ohlcvs)):
        list=[]
        for j in range(6):
            list.append(ohlcvs[i][j])
        writer.writerow(list)



for i in range(1,4):
    if(ohlcvs[-i][1]>ohlcvs[-i][4]):
        ohlcvs[-i].append('blue')
    else:
        ohlcvs[-i].append('red')

print(ohlcvs[-3])
print(ohlcvs[-2])
print(ohlcvs[-1])