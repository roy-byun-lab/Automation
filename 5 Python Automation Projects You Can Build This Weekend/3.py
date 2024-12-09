"""
Automatic Data Scraper

some price data on an e-commerce site or some stock market data can gather and piled up
With Python, BeautifulSoup, and requests libraries,it’s really easy to scrape and automate this process of data extraction

What You’ll Need:
    1.requests library (For making HTTP requests)
    2.BeautifulSoup from bs4 (For parsing HTML)
"""
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com/products"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find product names and prices
products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("h2").text
    price = product.find("span", class_="price").text
    print(f"Product: {name}, Price: {price}")
