import requests
import json

# Init

link = 'https://newsapi.org/v2/everything'
params = {
    'q': "+trump -opinion",                # keyword or phrase to search for
    'from': '2024-10-04',     # start date for the articles
    'sortBy': 'relevancy',    # sort articles by popularity, relevancy, or publishedAt
    'apiKey': 'e1fc83725afd4b75a0690f6253474549',
    'language': 'en',
    'excludeDomains': 'cnn.com, msnbc.com'
}

# Make a request to the API
def generate_newsdata(url=link, parameters=params):
    response = requests.get(url, params=parameters)
    data = response.json()
    results = {}
    
    for article in data['articles']:
        article['publishedAt'] = article['publishedAt'][:10]
        
    for article in data['articles']:
        if article['publishedAt'] not in results:
            results[article['publishedAt']] = []
        results[article['publishedAt']].append(article['description'])
        results[article['publishedAt']].append(article['title'])

    # Check if the request was successful
    if response.status_code == 200:
        # Print the entire JSON response
        with open('data.json', 'w') as outfile:
            json.dump(results, outfile, indent=4)

        with open('unparsed_data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

    else:
        print(f"Error: {response.status_code}")
    return results

generate_newsdata(link,params)
