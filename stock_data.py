import yfinance as yf
import datetime
import numpy as np

# Set the ticker symbol and date range
ticker = "DJT"
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)

# Fetch the data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# convert DataFrame to list
closing_prices_list = np.ravel(stock_data["Close"].values.tolist())
print(closing_prices_list)

closing_prices_list *= (1.0 / closing_prices_list.max())

print('\n')
print(closing_prices_list)