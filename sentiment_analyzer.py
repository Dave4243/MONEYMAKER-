from transformers import pipeline
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import newsdata
import stock_data

# Load a sentiment-analysis pipeline from transformers
sentiment_analyzer = pipeline("sentiment-analysis")


def analyze_sentiment(sentence):
    # Perform sentiment analysis
    result = sentiment_analyzer(sentence)
    
    score = result[0]['score']
    
    # includes 'label' and 'score'
    return score if result[0]['label'] == 'POSITIVE' else -score

# Example usage
# sentence = "hi!"
# print(analyze_sentiment(sentence))


# input map from date to array of headline/sentneces
# for reach sentence, compute the sentiment of that sentence
# average out the sentiments per each date
# returns a map from date to number representing the average sentiment for that day
def map_sentiments(input_dict):
  result = {}
  for date, arr in input_dict.items():
    total_sentiment = sum(analyze_sentiment(item) for item in arr)
    result[date] = total_sentiment / len(arr)
  return result


data = map_sentiments(newsdata.generate_newsdata())

def transform_to_array(avg_sentiment_dict=data):
  sorted_values = [value for key, value in sorted(avg_sentiment_dict.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m-%d'))]
  
# Then, we can compare this to the array of stock prices and create a plot
# of stock price (y) vs sentiment (x) per each day. Then, find the correlation.
def plot_and_find_correlation(avg_sentiments_dict=data, stock_data_array=stock_data.get_stock_data()):
  sentiments_array = transform_to_array(avg_sentiments_dict)
  plt(sentiments_array, stock_data_array)
  plt.show()
  return np.corrcoef(sentiments_array, stock_data_array)[0, 1]
  
plot_and_find_correlation()

# Even further, we could use a predictive model based on the data by calculating
# the mean change in the stock price based on the previous time's sentiments along
# with standard deviations

