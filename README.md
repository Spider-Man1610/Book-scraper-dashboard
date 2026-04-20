# Book Data Dashboard

A Python project that automatically collects book data from the web 
and displays it in an interactive dashboard.

## What it does
- Collects title, price, rating and availability of 100 books across 5 pages
- Saves the data to a CSV file
- Displays the data in an interactive Streamlit dashboard with charts and search

## How to run

### Step 1 - Collect the data
python Scraper.py

### Step 2 - Launch the dashboard
streamlit run dashboard.py

## Tech Stack
- Python
- BeautifulSoup4 - data collection
- Pandas - data storage and processing
- Streamlit - dashboard
- Plotly - charts