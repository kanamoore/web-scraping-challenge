#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time


# In[2]:


# Set up executable path
executable_path = {"executable_path": "C:/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# # NASA Mars News

# In[3]:


# Set up url
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[8]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.
html = browser.html
soup = BeautifulSoup(html, "html.parser")
results = soup.find("ul", class_="item_list")


# In[7]:


news_title = results.find("div", class_="content_title").text
news_p = results.find("div", class_="article_teaser_body").text

print(news_title)
print(news_p)


# In[ ]:





# In[9]:


# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."


# In[10]:


for item in range(1,3):
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find("ul", class_="item_list")
    time.sleep(1)
    
    for article in results:
        news_title = article.find("div", class_="content_title").text
        news_p = article.find("div", class_="article_teaser_body").text
        
        print(news_title)
        print(news_p)
    browser.links.find_by_partial_text('More')


# # JPL Mars Space Images - Featured Image

# In[11]:


# Set up url
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
url_root = url.split('/spaceimages')[0]
browser.visit(url)


# In[12]:


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


# In[ ]:





# In[13]:


browser.click_link_by_partial_text('FULL')
time.sleep(5)
browser.click_link_by_partial_text('more info')


# In[14]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")
img_result = soup.find("figure", class_="lede")
img_result


# In[15]:


# Find the image url to the full size .jpg image
featured_image_url = url_root + img_result.a["href"]
featured_image_url


# In[16]:



# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# Make sure to .
# Make sure to save a complete url string for this image.


# Example:


# # Mars Weather

# In[24]:


# Set up url
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_weather = soup.find_all('p', class_='TweetTextSize --normal js-tweet-text tweet-text')
# results = soup.find("section", aria-labelledby="accessible-list-5")
mars_weather


# In[ ]:





# In[27]:


mars_weather_tweet = soup.find("div", 
                                attrs={"aria-label": "accessible-list-6"})

# results = soup.find("div", results = soup.find("div", cla="css-1dbjc4n r-18u37iz r-thb0q2"))
mars_weather_tweet


# In[ ]:


mars_weather_tweet


# In[ ]:


mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
print(mars_weather)


# In[ ]:


# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'


# # Mars Facts

# In[ ]:


# Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
url = "https://space-facts.com/mars/"
facts_df = pd.read_html(url)[1].set_index("Mars - Earth Comparison")
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

# In[84]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
url_root = url.split('/search')[0]
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[85]:


url_root


# In[86]:


title_list = []
url_list = []
    
for result in range(1):
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("div", class_="item")
    
    # Get url for each hemisphere
    for item in results:
        item_url = item.a["href"]
        item_full_url = url_root + item_url
        url_list.append(item_full_url)
        title = item.find("h3").text
        title_list.append(title)
        
title_list


# In[87]:


url_list


# In[88]:


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


# In[96]:


hemisphere_image_urls = []

for url,title in zip(url_dict_list,title_list):
    hemisphere_image_dict = {}
    hemisphere_image_dict["title"] = title
    hemisphere_image_dict["img_url"] = url
    hemisphere_image_urls.append(hemisphere_image_dict)
    print(hemisphere_image_dict)


# In[97]:


hemisphere_image_urls


# In[ ]:


# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


# In[28]:


jupyter nbconvert --to script mission_to_mars.ipynb


# In[ ]:




