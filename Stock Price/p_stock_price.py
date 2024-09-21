import yfinance as yf

stock = input("enter stock ticker: ").upper()
price_info=yf.Ticker(stock).history(period="1d")
late_market_price= price_info['Close'].iloc[-1]
print("Last market price of", stock, "is", late_market_price)