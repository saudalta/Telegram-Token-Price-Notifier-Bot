import requests


def binance_config(ticker):  # defining key/request url
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker}USDT"
    data = requests.get(key)
    data = data.json()
    price = float(data['price'])
    return price
