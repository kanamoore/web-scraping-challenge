# Web Scraping Project - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this project, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Data Sources
All the data were scraped from the following websites:

* [NASA Mars News Site](https://mars.nasa.gov/news/) - Scraped the latest News Title and Paragraph Text
* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) - Scraped the image url for the current Featured Mars Image
* [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) - Scraped the latest Mars weather tweet
* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) - Scraped high resolution images for each of Mar's hemispheres
* [Mars Facts webpage](https://space-facts.com/mars/) -Scraped the table containing facts about the planet including Diameter, Mass, etc 

## Web Scraping
Completed an initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Jupyter Notebook file called `mission_to_mars.ipynb` have codes of my scraping and analysis tasks. The 


## MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
