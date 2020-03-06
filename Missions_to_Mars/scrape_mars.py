import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    executable_path = {"executable_path": "C:/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    # NASA Mars News
    browser = init_browser()
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    nasa_html = browser.html
    soup = BeautifulSoup(nasa_html, "html.parser")
    nasa_results = soup.find("ul", class_="item_list")
    news_title = nasa_results.find("div", class_="content_title").text
    news_p = nasa_results.find("div", class_="article_teaser_body").text
    print(news_title, news_p)
    return(news_title, news_p)

    # # JPL Mars Space Images - Featured Image
    # mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # mars_url_root = mars_url.split('/spaceimages')[0]
    # browser.visit(mars_url)
    # browser.click_link_by_partial_text('FULL')
    # time.sleep(5)
    # browser.click_link_by_partial_text('more info')
    # mars_html = browser.html
    # mars_soup = BeautifulSoup(mars_html, "html.parser")
    # mars_img_result = mars_soup.find("figure", class_="lede")
    # featured_image_url = mars_url_root + mars_img_result.a["href"]
    # print(featured_image_url)

    # Mars Weather
    # url = "https://twitter.com/marswxreport?lang=en"
    # browser.visit(url)

    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")
    # mars_weather = soup.find_all('p', class_='TweetTextSize --normal js-tweet-text tweet-text')
    # # results = soup.find("section", aria-labelledby="accessible-list-5")
    # mars_weather



    # mars_weather_tweet = soup.find("div", 
    #                                 attrs={"aria-label": "accessible-list-6"})

    # # results = soup.find("div", results = soup.find("div", cla="css-1dbjc4n r-18u37iz r-thb0q2"))


    # # Mars Facts
    # facts_url = "https://space-facts.com/mars/"
    # facts_df = pd.read_html(url)[1].set_index("Mars - Earth Comparison")
    # html_table = facts_df.to_html()
    # html_table.replace("\n","")
    # facts_df.to_html('table_v2.html')


    # # Mars Hemispheres
    # hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # h_url_root = hemisphere_url.split('/search')[0]
    # browser.visit(url)
    # # h_html = browser.html
    # # h_soup = BeautifulSoup(h_html, "html.parser")

    # title_list = []
    # url_list = []
        
    # for result in range(1):
    #     h_html = browser.html
    #     h_soup = BeautifulSoup(h_html, "html.parser")
    #     h_results = h_soup.find_all("div", class_="item")
        
    #     # Get url for each hemisphere
    #     for item in h_results:
    #         item_url = item.a["href"]
    #         item_full_url = h_url_root + item_url
    #         url_list.append(item_full_url)
    #         title = item.find("h3").text
    #         title_list.append(title)

    # # Get image url from each page and create url list
    # url_dict_list = []

    # for item_url in url_list:
    #     browser.visit(item_url)
    #     html = browser.html
    #     soup = BeautifulSoup(html, "html.parser")
    #     img_path = soup.select_one("ul")
    #     image_url = img_path.a["href"]
    #     url_dict_list.append(image_url)

    # hemisphere_image_urls = []

    # for url,title in zip(url_dict_list,title_list):
    #     hemisphere_image_dict = {}
    #     hemisphere_image_dict["title"] = title
    #     hemisphere_image_dict["img_url"] = url
    #     hemisphere_image_urls.append(hemisphere_image_dict)
    #     print(hemisphere_image_dict)

    mars_data_dict = {
        "news_title" : news_title,
        "news_paragraph" : news_p
        # "featured_image_url" : featured_image_url
    }

    print(mars_data_dict)
    return(mars_data_dict)