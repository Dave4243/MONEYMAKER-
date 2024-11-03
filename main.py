import newsdata
import stock_data
import matplotlib

link = 'https://newsapi.org/v2/everything'
ticker = "DJT"
days = 30
max_val = 1.0

params = {
    'q': 'trump',                # keyword or phrase to search for
    'from': '2024-10-03',     # start date for the articles
    'sortBy': 'publishedAt',    # sort articles by popularity, relevancy, or publishedAt
    'apiKey': 'e1fc83725afd4b75a0690f6253474549',
    'language': 'en'
}

stock_data.get_stock_data_normalized(ticker, days, max_val)
data = newsdata.generate_newsdata(link, params)

