from config import STOP_LOSS_PIPS, TAKE_PROFIT_PIPS

def get_sl_tp(price, action, sl_pips=STOP_LOSS_PIPS, tp_pips=TAKE_PROFIT_PIPS):
    point = 0.0001  # For EURUSD
    if action == 'BUY':
        sl = price - sl_pips * point
        tp = price + tp_pips * point
    else:
        sl = price + sl_pips * point
        tp = price - tp_pips * point
    return sl, tp