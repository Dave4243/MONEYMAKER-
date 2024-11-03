import newsdata
import stock_data
import sentiment_analyzer as sa

ticker = input("Stock ticker to analyze: ")
keyword = input("What keyword would you like the analyze?: ")

def get_ticker():
    return ticker

params = {
    'q': keyword,                # keyword or phrase to search for
    'from': '2024-10-04',     # start date for the articles
    'apiKey': 'e1fc83725afd4b75a0690f6253474549',
    'sortBy': 'relevancy',
    'language': 'en',
}

def get_params():
    return params

stocks = stock_data.get_stock_data(ticker = ticker)
news = sa.map_sentiments(newsdata.generate_newsdata(parameters = params))

sa.print_correlation(sentiments=news, stocks=stocks)