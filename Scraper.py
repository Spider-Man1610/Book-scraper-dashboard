import requests
from bs4 import BeautifulSoup
import pandas as pd

# The website we are srapping
BASE_URL="https://books.toscrape.com/catalogue/"
START_URL="https://books.toscrape.com/catalogue/page-1.html"

def scrape_books(url):
    response=requests.get(url)
    print(response)
    soup=BeautifulSoup(response.text,"html.parser")
    # print(soup.title)
    books=soup.find_all("article")   
    # print(len(books))
    print(books[0].find("h3"))
scrape_books(START_URL)