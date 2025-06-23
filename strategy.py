import pandas as pd
import MetaTrader5 as mt5
from config import SYMBOL, SHORT_MA, LONG_MA

def get_data(symbol=SYMBOL, timeframe=mt5.TIMEFRAME_M5, bars=100):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def check_signal(df):
    df['ma_short'] = df['close'].rolling(SHORT_MA).mean()
    df['ma_long'] = df['close'].rolling(LONG_MA).mean()

    if df['ma_short'].iloc[-2] < df['ma_long'].iloc[-2] and df['ma_short'].iloc[-1] > df['ma_long'].iloc[-1]:
        return 'BUY'
    elif df['ma_short'].iloc[-2] > df['ma_long'].iloc[-2] and df['ma_short'].iloc[-1] < df['ma_long'].iloc[-1]:
        return 'SELL'
    return 'HOLD'