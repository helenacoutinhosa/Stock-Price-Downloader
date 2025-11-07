import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# List of Brazilian assets to compare
assets = ["BOVA11.SA", "PETR4.SA", "VALE3.SA", "ITUB4.SA"]

# Download 1-year historical data for all assets
history = yf.download(assets, period="1y")["Close"]

# Display the first few rows
print("Closing price data (first rows):")
print(history.head())

# Normalize prices to compare performance
normalized = history / history.iloc[0]

# Plot comparative performance
plt.figure()
for ticker in normalized.columns:
    plt.plot(normalized.index, normalized[ticker], label=ticker)

plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.title("Comparative Performance of Selected Brazilian Assets (1 Year)")
plt.legend()
plt.show()