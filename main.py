# import requests
# from bs4 import BeautifulSoup

# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# # print content of request
# print(r.content)

import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')
content = s.find_all('p')

print(content)
