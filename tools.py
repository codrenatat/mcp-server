import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Función para obtener el precio actual de una acción
def get_current_price(symbol: str) -> str:
    apikey = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apikey}"
    )
    response = requests.get(url)
    data = response.json()

    if "Time Series (5min)" not in data:
        return "Error al obtener datos. Verifica el símbolo o tu API key."

    latest_time = sorted(data["Time Series (5min)"].keys())[-1]
    latest_price = data["Time Series (5min)"][latest_time]["4. close"]
    return f"Precio de {symbol} a las {latest_time} es ${latest_price}"
