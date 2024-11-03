from newsapi import NewsApiClient
import requests
import json

# Init
newsapi = NewsApiClient(api_key='e1fc83725afd4b75a0690f6253474549')

url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'trump',                # keyword or phrase to search for
    'from': '2024-10-03',     # start date for the articles
    'sortBy': 'relevancy',    # sort articles by popularity, relevancy, or publishedAt
    'category': 'general',
    'apiKey': 'e1fc83725afd4b75a0690f6253474549'
}

# Make a request to the API
response = requests.get(url, params=params)

data = {'': ''}

# Check if the request was successful
if response.status_code == 200:
    # Print the entire JSON response
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)