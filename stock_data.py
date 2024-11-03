import yfinance as yf
import datetime
import numpy as np

# ticker is a string
# num days is a int
# max_value is a double
def get_stock_data(ticker = "DJT", num_days = 30, max_value = 1.0):
  end_date = datetime.date.today()
  start_date = end_date - datetime.timedelta(days = num_days + 1)

  # Fetch the data
  stock_data = yf.download(ticker, start=start_date, end=end_date)

  # convert DataFrame to list
  closing_prices_list = np.ravel(stock_data["Close"].values.tolist())
  #print(closing_prices_list)
  
  result = []
  for i in range(len(closing_prices_list) - 1):
    diff = closing_prices_list[i + 1] - closing_prices_list[i]
    result.append(float(diff))
  # closing_prices_list *= (max_value / closing_prices_list.max())
  
  #print('\n')
  #print(result)
  return result 

get_stock_data("DJT", 30, 1.0)