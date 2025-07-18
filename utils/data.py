import yfinance as yf
import numpy as np
import streamlit as st

ASSETS = {"Stocks": "SPY", "Bonds": "BND", "Gold": "GLD", "Crypto": "BTC-USD"}
DEFAULT_RETURNS = [0.06, 0.04, 0.03, 0.10]
DEFAULT_VOL = [0.15, 0.07, 0.10, 0.50]

@st.cache_data
def fetch_asset_data():
    returns, volatilities = [], []
    for i, (name, ticker) in enumerate(ASSETS.items()):
        try:
            data = yf.download(ticker, period="6mo", interval="1d", progress=False)
            if data.empty or "Close" not in data:
                raise ValueError()
            ret = data["Close"].pct_change().dropna()
            annual_return = float(ret.mean() * 252)
            annual_vol = float(ret.std() * np.sqrt(252))

        except Exception:
            st.warning(f"⚠️ Using default data for {name}")
            annual_return, annual_vol = DEFAULT_RETURNS[i], DEFAULT_VOL[i]

        returns.append(annual_return)
        volatilities.append(annual_vol)
    return returns, volatilities
