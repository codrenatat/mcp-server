import os
import requests
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

def get_current_price(symbol: str) -> str:
    """
    Gets the current price of a stock from Alpha Vantage API.
    """
    apikey = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not apikey:
        return "Error: ALPHA_VANTAGE_API_KEY not configured"
    
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apikey}"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if there's an error in the response
        if "Error Message" in data:
            return f"Error: Symbol {symbol} is not valid"
        
        if "Note" in data:
            return "Error: API limit reached. Try again later."
        
        if "Time Series (5min)" not in data:
            return f"Error: Could not get data for {symbol}"
        
        # Get most recent price
        time_series = data["Time Series (5min)"]
        latest_time = sorted(time_series.keys())[-1]
        latest_data = time_series[latest_time]
        latest_price = latest_data["4. close"]
        
        return f"{symbol}: ${latest_price} (updated: {latest_time})"
        
    except requests.RequestException as e:
        return f"Connection error: {str(e)}"
    except Exception as e:
        return f"Data processing error: {str(e)}"
    
def get_currency_exchange_rate(from_currency: str, to_currency: str) -> dict:
    """Fetch exchange rate between two currencies from Alpha Vantage."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Realtime Currency Exchange Rate" in data:
            return data["Realtime Currency Exchange Rate"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_fx_daily_data(from_symbol: str, to_symbol: str) -> dict:
    """Fetch daily time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series FX (Daily)" in data:
            return data["Time Series FX (Daily)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_fx_weekly_data(from_symbol: str, to_symbol: str) -> dict:
    """Fetch weekly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FX_WEEKLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "apikey": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series FX (Weekly)" in data:
            return data["Time Series FX (Weekly)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_fx_monthly_data(from_symbol: str, to_symbol: str) -> dict:
    """Fetch monthly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FX_MONTHLY",
        "from_symbol": from_symbol,
        "to_symbol": to_symbol,
        "apikey": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series FX (Monthly)" in data:
            return data["Time Series FX (Monthly)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_digital_currency_daily_data(symbol: str, market: str) -> dict:
    """
    Fetch daily historical time series for a digital currency (e.g., BTC)
    traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC).
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": market,
        "apikey": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series (Digital Currency Daily)" in data:
            return data["Time Series (Digital Currency Daily)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_digital_currency_weekly_data(symbol: str, market: str) -> dict:
    """
    Fetch weekly historical time series for a digital currency (e.g., BTC)
    traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC).
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": symbol,
        "market": market,
        "apikey": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series (Digital Currency Weekly)" in data:
            return data["Time Series (Digital Currency Weekly)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_digital_currency_monthly_data(symbol: str, market: str) -> dict:
    """
    Fetch monthly historical time series for a digital currency (e.g., BTC)
    traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC).
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": symbol,
        "market": market,
        "apikey": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Check if the data contains the required information
        if "Time Series (Digital Currency Monthly)" in data:
            return data["Time Series (Digital Currency Monthly)"]
        else:
            return {"error": "Invalid data returned"}
    else:
        return {"error": "Failed to fetch data"}
    
def get_crude_oil_wti_data(interval: Optional[str]) -> dict:
    """
    Fetch the West Texas Intermediate (WTI) crude oil prices in daily, weekly, and monthly horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "WTI",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_crude_oil_brent_data(interval: Optional[str]) -> dict:
    """
    Fetch the Brent crude oil prices in daily, weekly, and monthly horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "BRENT",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_natural_gas_data(interval: Optional[str]) -> dict:
    """
    Fetch the natural Henry Hub gas prices in daily, weekly, and monthly horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "NATURAL_GAS",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()

    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_copper_data(interval: Optional[str]) -> dict:
    """
    Fetch the copper prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "COPPER",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_aluminum_data(interval: Optional[str]) -> dict:
    """
    Fetch the aluminum prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "ALUMINUM",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_wheat_data(interval: Optional[str]) -> dict:
    """
    Fetch the wheat prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "WHEAT",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_corn_data(interval: Optional[str]) -> dict:
    """
    Fetch the corn prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "CORN",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_cotton_data(interval: Optional[str]) -> dict:
    """
    Fetch the cotton prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "COTTON",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_sugar_data(interval: Optional[str]) -> dict:
    """
    Fetch the sugar prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "SUGAR",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_coffee_data(interval: Optional[str]) -> dict: 
    """
    Fetch the coffee prices in monthly, quarterly, and annual horizons.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "COFFEE",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_all_commodities_data(interval: Optional[str]) -> dict:
    """
    Fetch the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "ALL_COMMODITIES",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_real_gdp(interval: Optional[str]) -> dict:
    """
    Fetch the Real GDP of the US data in quarterly and annual temporal dimensions.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "REAL_GDP",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_real_gdp_per_capita() -> dict:
    """
    Fetch the quarterly Real GDP per Capita data of the United States..
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "REAL_GDP_PER_CAPITA",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_treasury_yield(interval: Optional[str], maturity: Optional[str]) -> dict:
    """
    Fetch the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TREASURY_YIELD",
        "interval": interval,
        "maturity": maturity,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_federal_funds_rate(interval: Optional[str]) -> dict:
    """
    Fetch the daily, weekly, and monthly federal funds rate (interest rate) of the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FEDERAL_FUNDS_RATE",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_cpi_data(interval: Optional[str]) -> dict:
    """
    Fetch the monthly and semiannual consumer price index (CPI) of the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "CPI",
        "interval": interval,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_inflation() -> dict:
    """
    Fetch the annual inflation rates (consumer prices) of the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "INFLATION",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_retail_sales() -> dict:
    """
    Fetch the monthly Advance Retail Sales: Retail Trade data of the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "RETAIL_SALES",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
    
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_durables() -> dict:
    """
    Fetch the monthly manufacturers' new orders of durable goods in the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "DURABLES",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_monthly_unemployment() -> dict:
    """
    Fetch the monthly unemployment rate of the US.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "UNEMPLOYMENT",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
    
def get_nonfarm_payroll() -> dict:
    """
    Fetch the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
    a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees,
    unpaid volunteers, farm employees, and the unincorporated self-employed.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "NONFARM_PAYROLL",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}