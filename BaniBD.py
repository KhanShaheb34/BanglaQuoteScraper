# Scrape quotes from https://bani.com.bd/
# Scrape with category and wirter

from bs4 import BeautifulSoup
import pandas as pd
import requests

counter = 0
quotes = []

while True:
    counter = counter + 1

    res = requests.get(f"https://bani.com.bd/1/{counter}/")
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        quote = soup.find('h2', class_='text-center').text[3:-3]
        writer = soup.find('h3').text
        categories = [cat.text for cat in soup.find_all('a', class_='label label-default cat clabel')]

        quotes.append([quote, writer, categories])
    except:
        pass
    
    print('.', end='')

    if counter % 100 == 0:
        pd.DataFrame(quotes).to_csv('quotes.csv', header=False, index=False, mode='a')
        quotes = []
        print()