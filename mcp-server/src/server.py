# Functions from the mcp python sdk 
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from tools import *

# Creating our MCP server
# Similar to FastAPI 
# If http specify port and host if not standart io 
mcp = FastMCP(
    name = "Alpha Vantage MCP Server",
    host = "0.0.0.0",   # Only used for SSE transport (localhost)
    port = 8050,    # Only used for SSE transport (set to any port)
)

app = FastAPI()

@mcp.tool()
@app.get("/get_current_price/{symbol}")
async def get_current_price_tool(symbol: str) -> str:
    """
    Gets the current price of a stock from Alpha Vantage API.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, GOOGL, MSFT)
    
    Returns:
        Current price formatted with timestamp
    """
    try:
        return get_current_price(symbol)
    except Exception as e:
        return f"Error getting price for {symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_currency_exchange_rate/{from_currency}/{to_currency}")
async def get_currency_exchange_rate_tool(from_currency: str, to_currency: str) -> dict:
    """
    Gets the current exchange rate between two currencies from Alpha Vantage API.
    
    Args:
        from_currency: Source currency (e.g.: USD, EUR)
    """
    try:
        return get_currency_exchange_rate(from_currency, to_currency)
    except Exception as e:
        return f"Error getting exchange rate for {from_currency} to {to_currency}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_daily_data/{from_symbol}/{to_symbol}")
async def get_fx_daily_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the daily time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_daily_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX daily data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_weekly_data/{from_symbol}/{to_symbol}")
async def get_fx_weekly_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the weekly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_weekly_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX weekly data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_monthly_data/{from_symbol}/{to_symbol}")
async def get_fx_monthly_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the monthly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_monthly_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX monthly data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_digital_currency_daily_data/{symbol}/{market}")
async def get_digital_currency_daily_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the daily historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_daily_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency daily data for {symbol} on {market}: {str(e)}"
    
@mcp.tool()
@app.get("/get_digital_currency_weekly_data/{symbol}/{market}")
async def get_digital_currency_weekly_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the weekly historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_weekly_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency weekly data for {symbol} on {market}: {str(e)}"

@mcp.tool()
@app.get("/get_digital_currency_monthly_data/{symbol}/{market}")
async def get_digital_currency_monthly_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the monthly historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_monthly_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency monthly data for {symbol} on {market}: {str(e)}"
    
@mcp.tool()
@app.get("/get_crude_oil_wti_data/")
async def get_crude_oil_wti_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the West Texas Intermediate (WTI) crude oil prices from Alpha Vantage API.
    """
    try:
        return get_crude_oil_wti_data(interval)
    except Exception as e:
        return f"Error getting crude oil WTI data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_crude_oil_brent_data/{interval}")
async def get_crude_oil_brent_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the Brent crude oil prices from Alpha Vantage API.
    """
    try:
        return get_crude_oil_brent_data(interval)
    except Exception as e:
        return f"Error getting crude oil Brent data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_natural_gas_data/{interval}")
async def get_natural_gas_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the natural gas prices from Alpha Vantage API.
    """
    try:
        return get_natural_gas_data(interval)
    except Exception as e:
        return f"Error getting natural gas data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_copper_data/{interval}")
async def get_copper_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of copper from Alpha Vantage API.
    """
    try:
        return get_copper_data(interval)
    except Exception as e:
        return f"Error getting copper data for {interval}: {str(e)}"

@mcp.tool()
@app.get("/get_aluminum_data/{interval}")
async def get_aluminum_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of aluminum from Alpha Vantage API.
    """
    try:
        return get_aluminum_data(interval)
    except Exception as e:
        return f"Error getting aluminum data for {interval}: {str(e)}"

@mcp.tool()
@app.get("get_wheat_data/{interval}")
async def get_wheat_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of wheat from Alpha Vantage API.
    """
    try:
        return get_wheat_data(interval)
    except Exception as e:
        return f"Error getting wheat data for {interval}: {str(e)}"

@mcp.tool()
@app.get("/get_corn_data/{interval}")
async def get_corn_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of corn from Alpha Vantage API.
    """
    try:
        return get_corn_data(interval)
    except Exception as e:
        return f"Error getting corn data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_cotton_data/{interval}")
async def get_cotton_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of cotton from Alpha Vantage API.
    """
    try:
        return get_cotton_data(interval)
    except Exception as e:
        return f"Error getting cotton data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_sugar_data/{interval}")
async def get_sugar_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of sugar from Alpha Vantage API.
    """
    try:
        return get_sugar_data(interval)
    except Exception as e:
        return f"Error getting sugar data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_coffee_data/{interval}")
async def get_coffee_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of coffee from Alpha Vantage API.
    """
    try:
        return get_coffee_data(interval)
    except Exception as e:
        return f"Error getting coffee data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_all_commodities_data/{interval}")
async def get_all_commodities_data_tool(interval: str) -> dict:
    """
    Gets the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.
    """
    try:
        return get_all_commodities_data(interval)
    except Exception as e:
        return f"Error getting all commodities data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_real_gdp_data/{interval}")
async def get_real_gdp_data_tool(interval: str) -> dict:
    """
    Gets the real GDP data of the US economy in quarterly and annual temporal dimensions.
    """
    try:
        return get_real_gdp(interval)
    except Exception as e:
        return f"Error getting real GDP data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_real_gdp_per_capita_data/")
async def get_real_gdp_per_capita_data_tool() -> dict:
    """
    Gets the real GDP per capita data quaterly of the US economy.
    """
    try:
        return get_real_gdp_per_capita()
    except Exception as e:
        return f"Error getting real GDP per capita data: {str(e)}"
    
@mcp.tool()
@app.get("get_treasury_yield/{interval}-{maturity}")
async def get_treasury_yield_tool(interval: str, maturity: str) -> dict:
    """
    Gets the US Treasury yield data for a specific maturity and interval.
    
    Args:
        interval: Interval of the data (e.g.: daily, weekly, monthly)
        maturity: Maturity of the treasury yield (e.g.: 10Y, 30Y)
    
    Returns:
        Treasury yield data
    """
    try:
        return get_treasury_yield(interval, maturity)
    except Exception as e:
        return f"Error getting treasury yield data for {maturity} at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_federal_funds_rate/{interval}")
async def get_federal_funds_rate_tool(interval: str) -> dict:
    """
    Gets the Federal Funds Rate in the US data for a specific interval.
    
    Args:
        interval: Interval of the data (e.g.: daily, weekly, monthly)
    
    Returns:
        Federal Funds Rate data
    """
    try:
        return get_federal_funds_rate(interval)
    except Exception as e:
        return f"Error getting Federal Funds Rate data at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_cpi_data/{interval}")
async def get_cpi_data_tool(interval: str) -> dict:
    """
    Gets the Consumer Price Index (CPI) data in the US for a specific interval.
    
    Args:
        interval: Interval of the data (monthly and semi-annual)
    
    Returns:
        CPI data
    """
    try:
        return get_cpi_data(interval)
    except Exception as e:
        return f"Error getting CPI data at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_inflation_data")
async def get_inflation_data_tool() -> dict:
    """
    Gets the inflation rate data in the US.
    """
    try:
        return get_inflation()
    except Exception as e:
        return f"Error getting inflation data: {str(e)}"

@mcp.tool()
@app.get("/get_retail_sales")
async def get_retail_sales_tool() -> dict:
    """
    Gets the monthly retail sales data in the US.
    """
    try:
        return get_retail_sales()
    except Exception as e:
        return f"Error getting retail sales data: {str(e)}"
    
@mcp.tool()
@app.get("/get_durables")
async def get_durables_tool() -> dict:
    """
    Gets the monthly manufacturers' new orders of durable goods in the US.
    """
    try:
        return get_durables()
    except Exception as e:
        return f"Error getting durable goods data: {str(e)}"
    
@mcp.tool()
@app.get("get_monthly_unemployment_rate")
async def get_monthly_unemployment_rate_tool() -> dict:
    """
    Gets the monthly unemployment rate in the US.
    """
    try:
        return get_monthly_unemployment()
    except Exception as e:
        return f"Error getting monthly unemployment rate data: {str(e)}"
    
@mcp.tool()
@app.get("/get_nonfarm_payrolls")
async def get_nonfarm_payrolls_tool() -> dict:
    """
    Gets the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
    a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees,
    unpaid volunteers, farm employees, and the unincorporated self-employed.
    """
    try:
        return get_nonfarm_payroll()
    except Exception as e:
        return f"Error getting non-farm payrolls data: {str(e)}"

# Run the server
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running mcp server with stdio transport")
        mcp.run(transport = "stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport = "sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
