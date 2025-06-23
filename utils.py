import MetaTrader5 as mt5
from config import LOT, SYMBOL
from risk_management import get_sl_tp

def place_order(signal):
    price = mt5.symbol_info_tick(SYMBOL).ask if signal == 'BUY' else mt5.symbol_info_tick(SYMBOL).bid
    sl, tp = get_sl_tp(price, signal)
    order_type = mt5.ORDER_TYPE_BUY if signal == 'BUY' else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 10032025,
        "comment": "MA crossover bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    print("Trade Result:", result)