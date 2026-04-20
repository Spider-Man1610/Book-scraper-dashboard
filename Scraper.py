import requests
from bs4 import BeautifulSoup
import pandas as pd

# The website we are srapping
BASE_URL="https://books.toscrape.com/catalogue/"
START_URL="https://books.toscrape.com/catalogue/page-1.html"

# Scapre info method or function
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    
    results = []
    # lOOp through every bOOk on the page 
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="availability").text.strip()
        
        # Appending the books info in a dict-list
        results.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
        })

    # Retruning data in DF
    return pd.DataFrame(results)

# Saving the data method
def save_data(df):
    df.to_csv("data/books.csv",index=False)
    print("Data saved to data/books.csv")

all_books=[]
# Each websites 50 sites all books info scrapping
for i in range(1,6):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"
    df=scrape_books(url)
    all_books.append(df)

# Sum up them all 
all=pd.concat(all_books)
save_data(all)