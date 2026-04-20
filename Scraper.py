import requests
from bs4 import BeautifulSoup
import pandas as pd

# The website we are srapping
BASE_URL="https://books.toscrape.com/catalogue/"
START_URL="https://books.toscrape.com/catalogue/page-1.html"

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    
    results = []
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="availability").text.strip()
        
        results.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
        })

    return pd.DataFrame(results)

def save_data(df):
    df.to_csv("data/books.csv",index=False)
    print("Data saved to data/books.csv")

all_books=[]

for i in range(1,6):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"
    df=scrape_books(url)
    all_books.append(df)
    
all=pd.concat(all_books)
save_data(all)