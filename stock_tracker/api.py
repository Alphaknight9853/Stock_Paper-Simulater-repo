import requests
from config import API_KEY, BASE_URL

def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise ValueError("Invalid stock symbol or API limit reached")

    return data["Time Series (Daily)"]
