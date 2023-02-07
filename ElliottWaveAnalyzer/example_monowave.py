from models.MonoWave import MonoWaveDown, MonoWaveUp
from models.helpers import plot_monowave
import numpy as np
import pandas as pd

import yfinance as yf
import datetime


startDate = datetime.datetime(2018, 7, 1)
endDate = datetime.datetime(2021, 7, 31)

# df = pd.read_csv(r'data\btc-usd_1d.csv')
company = yf.Ticker("RELIANCE.NS")
# company = yf.Ticker("PETRONET.NS")
# company = yf.Ticker("BPCL.NS")
# company = yf.Ticker("HINDPETRO.NS")
# company = yf.Ticker("IOC.NS")
# company = yf.Ticker("OIL.NS")
# company = yf.Ticker("ONGC.NS")
df = company.history(period="max",start=startDate, end=endDate)
df = df.reset_index()
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

lows = np.array(list(df['Low']))
highs = np.array(list(df['High']))
dates = np.array(list(df['Date']))

# find a monowave down starting from the low at the 3rd index
mw_up = MonoWaveUp(lows=lows, highs=highs, dates=dates, idx_start=3, skip=5)
plot_monowave(df, mw_up)

# find a monowave down from the end of the monowave up
mw_down = MonoWaveDown(lows=lows, highs=highs, dates=dates, idx_start=mw_up.idx_end, skip=0)
plot_monowave(df, mw_down)