#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests


# In[ ]:


# Set up executable path
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# # NASA Mars News

# In[ ]:


# Set up url
nasa_url = "https://mars.nasa.gov/news/"
browser.visit(nasa_url)


# In[ ]:


# Scrape html and fine item list
nasa_html = browser.html
nasa_soup = BeautifulSoup(nasa_html, "html.parser")
nasa_results = nasa_soup.find("ul", class_="item_list")


# In[ ]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
news_title = nasa_results.find("div", class_="content_title").text
news_p = nasa_results.find("div", class_="article_teaser_body").text

print(news_title)
print(news_p)


# # JPL Mars Space Images - Featured Image

# In[ ]:


# Set up url
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
jpl_url_root = jpl_url.split('/spaceimages')[0]
browser.visit(jpl_url)


# In[ ]:


# Click full image and more info to get image url
browser.click_link_by_partial_text('FULL')
time.sleep(5)
browser.click_link_by_partial_text('more info')


# In[ ]:


# Find figure to retrieve section that has image url
jpl_html = browser.html
jpl_soup = BeautifulSoup(jpl_html, "html.parser")
jpl_img_result = jpl_soup.find("figure", class_="lede")
jpl_img_result


# In[ ]:


# Find the image url to the full size .jpg image
featured_image_url = jpl_url_root + jpl_img_result.a["href"]
featured_image_url


# In[ ]:


## If there is an error, use this intead ##
# jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# jpl_url_root = url.split('/spaceimages')[0]
# browser.visit(jpl_url)
# html = browser.html
# soup = BeautifulSoup(html, "html.parser")
# result = soup.find("a", class_="button fancybox")
# # Visit the url for JPL Featured Space Image here.
# results = soup.find("a", class_="button fancybox")
# img_url = url_root + results["data-link"]
# # browser.visit(img_url)
# Find the image url to the full size .jpg image
# html = browser.html
# soup = BeautifulSoup(html, "html.parser")
# img_result = soup.find("figure", class_="lede")
# featured_image_url = url_root + img_result.a["href"]
# featured_image_url


# # Mars Weather

# In[ ]:


# Set up url and scrape latest tweets
twitter_url = "https://twitter.com/marswxreport?lang=en"
twitter_response = requests.get(twitter_url)
soup_twitter = BeautifulSoup(twitter_response.text, "html.parser")
tweets = soup_twitter.find_all('div', class_='js-tweet-text-container')


# In[ ]:


# Retrive tweets with weather information. Remove picture in the end
for tweet in tweets:
    mars_weather = tweet.find('p').text
    if 'sol' in mars_weather:
        mars_weather_tweet = mars_weather.split("pic.twitter")[0]
        print(mars_weather_tweet)
        break
    else:
        pass


# # Mars Facts

# In[ ]:


# Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
facts_url = "https://space-facts.com/mars/"
facts_df = pd.read_html(facts_url)[1].set_index("Mars - Earth Comparison")
facts_df


# In[ ]:


# Use Pandas to convert the data to a HTML table string.
html_table = facts_df.to_html()
html_table


# In[ ]:


# Strip newlines
html_table.replace("\n","")


# In[ ]:


# Save html table
facts_df.to_html('table_v2.html')


# # Mars Hemispheres

# In[ ]:


# Visit the USGS Astrogeology site 
h_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
h_url_root = h_url.split('/search')[0]
browser.visit(h_url)


# In[ ]:


# Scrape the site and visit each hemisphere page
title_list = []
url_list = []
    
for result in range(1):
    h_html = browser.html
    h_soup = BeautifulSoup(h_html, "html.parser")
    h_results = h_soup.find_all("div", class_="item")
    
    # Get url for each hemisphere
    for item in h_results:
        item_url = item.a["href"]
        item_full_url = h_url_root + item_url
        url_list.append(item_full_url)
        title = item.find("h3").text
        title_list.append(title)
        
title_list


# In[ ]:


# Get image url from each page and create url list
url_dict_list = []

for item_url in url_list:
    browser.visit(item_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    img_path = soup.select_one("ul")
    image_url = img_path.a["href"]
    url_dict_list.append(image_url)
    
url_dict_list


# In[ ]:


# Combine 2 lists to get one list of dictionaries
hemisphere_image_urls = []

for url,title in zip(url_dict_list,title_list):
    hemisphere_image_dict = {}
    hemisphere_image_dict["title"] = title
    hemisphere_image_dict["img_url"] = url
    hemisphere_image_urls.append(hemisphere_image_dict)
print(hemisphere_image_urls)

