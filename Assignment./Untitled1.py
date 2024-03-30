#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a python program to display IMDB’s Top rated 100 Indian movies’ data https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/list/ls056092300/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

movie_containers = soup.find_all("div", class_="lister-item-content")

names = []
ratings = []
years = []

for container in movie_containers:
    # Extract movie name
    name = container.find("a").text.strip()
    names.append(name)
    
    # Extract movie rating
    rating = container.find("span", class_="ipl-rating-star__rating").text.strip()
    ratings.append(rating)
    
    # Extract year of release
    year = container.find("span", class_="lister-item-year").text.strip()
    years.append(year)


data = {
    "Name": names,
    "Rating": ratings,
    "Year of Release": years
}
df = pd.DataFrame(data)

print(df)


# In[ ]:


# Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the heading, date, content and the likes for the video from the link for the youtube video from the post.

import requests
from bs4 import BeautifulSoup


patreon_url = "https://www.patreon.com/coreyms"
page = requests.get(patreon_url)
soup = BeautifulSoup(page.content, 'html.parser')


post_details = []
for post in soup.find_all('article'):
    heading = post.h2.text.strip()
    date = post.find('time', class_='entry-time').text.strip()
    content = post.find('div', class_='entry-content').text.strip()
   

video_container = soup.find('div', class_='video-container')
if video_container:
    youtube_video_url = video_container.find('iframe')['src']

else:
    youtube_video_url = None
import pandas as pd


columns = ['Heading', 'Date', 'Content', 'YouTube Video URL']
df = pd.DataFrame(post_details, columns=columns)


print(df)


# In[ ]:


# Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar. 

import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://www.nobroker.in/"


localities = ["Indira Nagar", "Jayanagar", "Rajaji Nagar"]


titles = []
locations = []
areas = []
emis = []
prices = []


for locality in localities:
    search_url = f"{url}property/sale/{locality}-bangalore"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")

    
    for card in soup.find_all("div", class_="card"):
        title = card.find("h2", class_="heading").text.strip()
        location = card.find("div", class_="nb__2CMjv").text.strip()
        area = card.find("div", class_="nb__3oNyC").text.strip()
        emi = card.find("div", class_="nb__2NPHR").text.strip()
        price = card.find("div", class_="nb__2NPHR").find_next("div").text.strip()

        titles.append(title)
        locations.append(location)
        areas.append(area)
        emis.append(emi)
        prices.append(price)


house_df = pd.DataFrame({
    "Title": titles,
    "Location": locations,
    "Area": areas,
    "EMI": emis,
    "Price": prices
})


print(house_df)


# In[ ]:


# Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/bestseller?sort=popular . 

import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.bewakoof.com/bestseller?sort=popular"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


product_names = []
product_prices = []
image_urls = []


product_containers = soup.find_all("div", class_="product-card")

for product in product_containers[:10]:
    # Product name
    name_box = product.find("h3", class_="product-card-title")
    product_name = name_box.text.strip()
    product_names.append(product_name)

    # Product price
    price_box = product.find("span", class_="product-card-price")
    product_price = price_box.text.strip()
    product_prices.append(product_price)

    # Image URL
    image_box = product.find("img", class_="product-card-image")
    image_url = image_box["src"]
    image_urls.append(image_url)


product_df = pd.DataFrame({
    "Product Name": product_names,
    "Price": product_prices,
    "Image URL": image_urls
})


print(product_df)


# In[ ]:


#  Please visit https://www.cnbc.com/world/?region=world and scrap-

import pandas as pd
import requests
from bs4 import BeautifulSoup

cnbc_url = "https://www.cnbc.com/world/?region=world"

response = requests.get(cnbc_url)
soup = BeautifulSoup(response.content, "html.parser")

headings = [headline.text.strip() for headline in soup.find_all("span", class_="Card-title")]
dates = [date.text.strip() for date in soup.find_all("time", class_="Card-time")]
news_links = [link["href"] for link in soup.find_all("a", class_="Card-titleLink")]

# Create a dataframe
df = pd.DataFrame({"Headings": headings, "Date": dates, "News Link": news_links})

print(df.head())


# In[ ]:


#  Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/ and scrap- 

import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"

response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")

paper_titles = []
authors = []
published_dates = []
paper_urls = []


article_containers = soup.find_all("div", class_="article-item")


for article in article_containers:
    # Paper title
    title = article.find("h3").text.strip()
    paper_titles.append(title)

    # Authors
    author = article.find("span", class_="author-name").text.strip()
    authors.append(author)

    # Published date
    date = article.find("span", class_="published-date").text.strip()
    published_dates.append(date)

    # Paper URL
    paper_url = article.find("a", class_="article-title")["href"]
    paper_urls.append(paper_url)


df = pd.DataFrame({
    "Paper Title": paper_titles,
    "Authors": authors,
    "Published Date": published_dates,
    "Paper URL": paper_urls
})


print(df)


# In[ ]:





# In[ ]:




