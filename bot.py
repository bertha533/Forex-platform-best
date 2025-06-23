import MetaTrader5 as mt5
import time
from config import *
from strategy import get_data, check_signal
from utils import place_order

def login():
    if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
        print("Login failed:", mt5.last_error())
        quit()

def run_bot():
    print("Starting trading bot...")
    while True:
        df = get_data()
        signal = check_signal(df)
        print(f"Signal: {signal}")
        if signal in ['BUY', 'SELL']:
            place_order(signal)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    login()
    run_bot()