from transformers import pipeline
import datetime
import matplotlib.pyplot as plt
import numpy as np
# Load a sentiment-analysis pipeline from transformers
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(sentence):
    # Perform sentiment analysis
    result = sentiment_analyzer(sentence)
    
    # includes 'label' and 'score'
    return result[0]

# Example usage
# sentence = "hi!"
# print(analyze_sentiment(sentence))


# input map from date to array of headline/sentneces
# for reach sentence, compute the sentiment of that sentence
# average out the sentiments per each date
# returns a map from date to number representing the average sentiment for that day
def map_sentiments(input_dict):
  result = {}
  for date, arr in input_dict:
    total_sentiment = sum(analyze_sentiment(str) for str in arr)
    result[date] = total_sentiment / len(arr)
  return result

def transform_to_array(avg_sentiment_dict):
  sorted_values = [value for key, value in sorted(avg_sentiment_dict.items(), key=lambda item: datetime.strptime(item[0], '%Y-%m-%d'))]
  
# Then, we can compare this to the array of stock prices and create a plot
# of stock price (y) vs sentiment (x) per each day. Then, find the correlation.
def plot_and_find_correlation(sentiments_dict, stock_data_array):
  sentiments_array = transform_to_array(sentiments_dict)
  plt(sentiments_array, stock_data_array)
  return np.corrcoef(sentiments_array, stock_data_array)[0, 1]
  

# Even further, we could use a predictive model based on the data by calculating
# the mean change in the stock price based on the previous time's sentiments along
# with standard deviations

