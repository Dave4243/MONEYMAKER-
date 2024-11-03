from transformers import pipeline

# Load a sentiment-analysis pipeline from transformers
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(sentence):
    # Perform sentiment analysis
    result = sentiment_analyzer(sentence)
    
    # includes 'label' and 'score'
    return result[0]

# Example usage
sentence = "hi!"
print(analyze_sentiment(sentence))


# input map from date to array of headline/sentneces
# for reach sentence, compute the sentiment of that sentence
# average out the sentiments per each date
# returns a map from date to number representing the sentiment for that day


# Then, we can compare this to the array of stock prices and create a plot
# of stock price (y) to sentiment (x) per each day. Then, find the correlation.


# Even further, we could use a predictive model based on the data by calculating
# the mean change in the stock price based on the previous time's sentiments along
# with standard deviations

