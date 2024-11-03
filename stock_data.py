import yfinance as yf
import datetime
import numpy as np

# ticker is a string
# num days is a int
# max_value is a double
def get_stock_data_normalized(ticker, num_days, max_value):
  end_date = datetime.date.today()
  start_date = end_date - datetime.timedelta(days = num_days)

  # Fetch the data
  stock_data = yf.download(ticker, start=start_date, end=end_date)

  # convert DataFrame to list
  closing_prices_list = np.ravel(stock_data["Close"].values.tolist())
  print(closing_prices_list)

  closing_prices_list *= (max_value / closing_prices_list.max())

  print('\n')
  print(closing_prices_list)

get_stock_data_normalized("DJT", 30, 1.0)