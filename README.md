# BanglaQuoteScraper

Scrape Bangla quotes from [bongquotes.com](https://bongquotes.com/) and [bani.com.bd](https://bani.com.bd/).

Used Python BeautifulSoup for scraping data from the sites.

### Scraped Data

- [2677 Quotes with Writer Name and Tags from bani.com.bd](data/banibd.csv)
- [1375 Quotes from bongquotes.com](data/bongquotes.csv)

### Usage

You can read the data using any csv reader. For example in python:

```py
import pandas as pd

banibd_data = pd.read_csv('data/banibd.csv')
bongquotes_data = pd.read_csv('data/bongquotes.csv')
```
