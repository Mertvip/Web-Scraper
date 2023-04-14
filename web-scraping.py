import requests
from bs4 import BeautifulSoup

# URL of the website to scrape data from
url = ' Website URL '

# Send GET request to the website
response = requests.get(url)

# Use BeautifulSoup to parse the HTML code of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the website
title = soup.title.text

# Extract the text content of the website
text = soup.get_text()

# Print the obtained data to the console
print('Title: ', title)
print('Text: ', text)
