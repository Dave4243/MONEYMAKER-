import requests
import json

# Init

link = 'https://newsapi.org/v2/everything'
params = {
    'q': 'trump',                # keyword or phrase to search for
    'from': '2024-10-03',     # start date for the articles
    'sortBy': 'publishedAt',    # sort articles by popularity, relevancy, or publishedAt
    'apiKey': 'e1fc83725afd4b75a0690f6253474549',
    'language': 'en'
}

# Make a request to the API
def generate_newsdata(url, parameters):
    response = requests.get(url, params=parameters)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Print the entire JSON response
        with open('data.json', 'w') as outfile:
            json.dump(response.json(), outfile, indent=4)
    else:
        print(f"Error: {response.status_code}")

generate_newsdata(link, params)