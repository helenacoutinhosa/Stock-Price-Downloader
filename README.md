# Brazilian Market Analysis 

This project analyzes the performance of key Brazilian financial assets over the past year.  
Using Python and public market datasets, it compares how major stocks and an ETF evolved in price relative to one another.

---

## Objective

To visually compare the performance of selected Brazilian market assets and understand their relative price trends over time.

---

## Assets Analyzed

| Ticker | Company / ETF | Description |
|-------|----------------|-------------|
| **BOVA11.SA** | iShares Ibovespa ETF | Tracks the Ibovespa index (Brazil stock market benchmark) |
| **PETR4.SA** | Petrobras (PN) | Oil & gas sector |
| **VALE3.SA** | Vale S.A. | Mining & commodities |
| **ITUB4.SA** | Itaú Unibanco | Banking & financial sector |

---

## Technologies Used

- Python
- pandas
- matplotlib
- yfinance

---

## How It Works

1. Fetches the last 1 year of historical price data for each asset.
2. Extracts and aligns closing prices.
3. Normalizes price series to compare performance on a relative scale.
4. Plots all normalized price series on one graph.

Normalization allows comparison even if assets have different absolute prices.

---

## Running the Script

If you're running this in a cloud environment (such as GitHub Codespaces, Google Colab, etc.), install the required libraries:

```bash
pip install yfinance pandas matplotlib

