import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# App title
st.header('Indian Stock Dashboard')

# User input from sidebar
ticker = st.sidebar.text_input('Symbol Code', 'INFY')
exchange = st.sidebar.text_input('Exchange', 'NSE')

# URL for scraping Google Finance
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

# Send request and parse HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
try:
    price = float(soup.find(class_='YMlKec fxKbKc').text.strip()[1:].replace(",", ""))
    previous_close = float(soup.find(class_='P6K39c').text.strip()[1:].replace(",", ""))
    revenue = soup.find(class_='QXDmN').text
    news = soup.find(class_='Yfwt5').text
    about = soup.find(class_='bLLb2d').text
except Exception as e:
    st.error(f"Error extracting data: {e}")
    st.stop()

# Store in dictionary
dict1 = {
    'Price': price,
    'Previous Price': previous_close,
    'Revenue': revenue,
    'News': news,
    'About': about
}

# Convert to DataFrame
df = pd.DataFrame(dict1, index=['Extracted Data']).T

# Display the data
st.write(df)
