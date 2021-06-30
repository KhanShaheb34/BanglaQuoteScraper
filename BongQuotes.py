# Scrape quotes from https://bongquotes.com/

from bs4 import BeautifulSoup
import pandas as pd
import requests

# Scraping the page links with quotes  
links = []
for page in range(1, 9):
    res = requests.get(f"https://bongquotes.com/category/quotes/page/{page}")
    soup = BeautifulSoup(res.text, 'html.parser')
    section = soup.find('section', class_='articles-wrapper')
    linkset = set([link['href'] for link in section.find_all('a')])
    for link in linkset:
        if link.split('/')[-3] != 'page':
            links.append(link)

# Scraping the quotes
for link in links:
    res = requests.get(f"https://bongquotes.com/bengali-quotes-about-life/")
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        quotes = [q.text.strip() for q in soup.find('ul', class_='quote-list').find_all('li')]
        pd.DataFrame(quotes).to_csv('bongquotes.csv', header=False, index=False, mode='a')
    except:
        pass