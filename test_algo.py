

# from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import streamlit as st


from io import BytesIO
import wikipedia





wikipedia.set_lang("en")

stock_symbol = "TATASTEEL.NS"
stocks_start_date = datetime.datetime(2023, 1, 1)
today = datetime.datetime.today()

#assets =['AAPL','AMZN','GOOG','NFLX']
stocksstartdate='2023-08-28'

def get_stock_data(stock_input,start_date,end_date):
  df[stock_input] = yf.download(stock_input, start=start_date, end=end_date)['Adj Close']      #fakta adj close
  return df


def closely(stock_input):                                                     # High deto
    df=yf.download(stock_input, start=stocksstartdate, end=today)['Low']
    return df

def complete_stock_data(stock_input,start_date,end_date):                                          #full complete deto
    df = yf.download(stock_input, start=start_date, end=end_date)
    return df

def High_data(vol_input,start_date,end_date):                                          #full complete deto
    ab[vol_input] = yf.download(vol_input, start=start_date, end=end_date)['High']
    return ab

def Low_data(stock_input,start_date,end_date):                                          #full complete deto
    df= yf.download(stock_input, start=start_date, end=end_date)['Volume']
    return ab
#ab[stock_input]
def full_exceptVolume(stock_input,start_date,end_date):                       # volume nai det bas
    df = yf.download(stock_input, start=start_date, end=end_date)
    df = df.drop(columns=['Volume'])
    return df

def get_sector_info(stock_symbol):
    try:
        # Create a Ticker object for the stock
        stock = yf.Ticker(stock_symbol)

        # Fetch the sector information
        sector = stock.info.get("industry", "Sector information not available")

        return sector

    except Exception as e:
        return f"Error retrieving sector information for {stock_symbol}: {str(e)}"

def get_stock_name(stock_symbol):
    try:
        # Create a Ticker object for the stock
        stock = yf.Ticker(stock_symbol)

        # Fetch the stock's full name or company name
        stock_info = stock.info
        company_name = stock_info.get("longName", "Stock name not available")

        return company_name

    except Exception as e:
        return f"Error retrieving stock name for {stock_symbol}: {str(e)}"

# stock_data = get_stock_data('m&m.ns', 2023-8-28,2023-11-5)
# HIGHdf = High_data('m&m.ns', 2023-8-28,2023-11-5)
# print(stock_data)
# print(HIGHdf)

# yf_ticker=yf.Ticker("SPY")
# print(yf_ticker)
# apple = yf.Ticker("AAPL")
#
# # Get historical data
# historical_data = apple.history(period="1y")
#
# # Get company information
# company_info = apple.info
#
# # Get recommendations
# recommendations = apple.recommendations
#
# # Get sustainability data
# sustainability_data = apple.sustainability
#
# # Get options data
# options_data = apple.options


# Example usage
#Welcome to Alpha Vantage! Here is your API key: IEVZD2BB8XP6DAB1. Please record this API key at a safe place for future data access.
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

# msft = yf.Ticker("MSFT")
#
# # get all stock info
# pp=msft.info
#
# # get historical market data
# hist = msft.history(period="1mo")
#
# # show meta information about the history (requires history() to be called first)
# msft.history_metadata
#
# print(hist)
# print("\n")
# print(pp)


low = pd.DataFrame()
ab=pd.DataFrame()
df = pd.DataFrame()



