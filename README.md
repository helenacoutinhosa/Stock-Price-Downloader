# Stock-Price-Downloader
Pull stock/crypto prices using yfinance, calculate returns, and plot results.

# Brazilian Stock Price Downloader
This Python script downloads historical stock data for Brazilian assets (e.g., PETR4.SA, VALE3.SA) using the `yfinance` API.

### Features
- Downloads 1 year of price data
- Calculates daily returns
- Plots price and return charts
- Saves the full dataset to CSV

### How to Use
pip install yfinance pandas matplotlib
python main.py

### Example Tickers
| Company | Ticker |
|--------|--------|
| Petrobras PN | PETR4.SA |
| Vale ON | VALE3.SA |
| Itaú Unibanco PN | ITUB4.SA |
| Ambev ON | ABEV3.SA |
