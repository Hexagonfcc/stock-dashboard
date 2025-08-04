import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Indian Stock Dashboard", layout="wide")

st.title("📈 Indian Stock Dashboard")

# Input
stock_symbol = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS, TCS.NS, INFY.NS):", "RELIANCE.NS")

if stock_symbol:
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

        st.subheader(f"{stock_info['longName']} ({stock_info['symbol']})")

        # Stock details
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"₹{stock_info['currentPrice']}")
        col2.metric("Market Cap", f"₹{stock_info['marketCap']:,}")
        col3.metric("52W High / Low", f"₹{stock_info['fiftyTwoWeekHigh']} / ₹{stock_info['fiftyTwoWeekLow']}")

        # Chart
        hist = stock.history(period="6mo")
        st.line_chart(hist['Close'])

        # Table
        st.subheader("Recent Data")
        st.dataframe(hist.tail(10))

    except Exception as e:
        st.error(f"⚠️ Failed to fetch data. Error: {e}")
else:
    st.info("Enter a valid NSE stock symbol to get started.")
