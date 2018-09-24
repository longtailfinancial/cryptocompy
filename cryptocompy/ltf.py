
import requests
import pandas as pd
import datetime
from . import top

def write_top_pricematrix(tsym='BTC', limit=20, exchange=''):
    pm = get_top_pricematrix()
    df = pd.DataFrame(pm)
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    df.to_csv(filename + ".csv")

def get_top_pricematrix(tsym='BTC', limit=20, exchange=''):
    symbols = get_top_symbols(tsym, limit)
    pm = get_pricematrix(symbols, exchange)
    return pm

def get_top_symbols(tsym='BTC', limit=20):
    coins = pd.DataFrame(top.get_top_coins(tsym='BTC', limit=20))
    symbols = list(coins['SYMBOL'].values[1:])
    return symbols

def get_pricematrix(symbols, exchange=''):
    """Get a matrix of trade pair rates where row and column indices of the
    matrix are symbols."""
    symbols_string = ','.join(symbols).upper()
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={0}&tsyms={0}'\
            .format(symbols_string)
    if exchange:
        url += '&e='.formate(exchange)
    page = requests.get(url)
    data = page.json()
    return data
