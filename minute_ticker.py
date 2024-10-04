import streamlit as st
import yfinance as yf
import pandas as pd
import time

# List of tickers
tickers = ["SOXL", "AAPL", "MSFT", "GOOGL"]

# Function to fetch data
def fetch_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data[ticker] = stock.history(period="1d", interval="1m")
    return data

# Streamlit app
st.title("Real-Time Stock Data")

# Display data
placeholder = st.empty()

while True:
    data = fetch_data(tickers)
    df = pd.concat(data, axis=1)
    placeholder.dataframe(df)
    time.sleep(60)  # Wait for 1 minute
