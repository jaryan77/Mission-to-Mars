# Mission to Mars (web-scraping-challenge) - Alex Ryan

# Summary
The purpose of this project is to design a web application that scrapes various Mars-related websites that displays the information in a single HTML page. Flask is used to deploy the scraped data to the HTML page. Using Bootstrap, a "Scrape New Data" button on the HTML page can be used to re-scrape the sites below to ensure all information is up-to-date.

#
# Data
--[NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)

* Collect latest News Title and Paragraph Text

--[JPL Featured Space Image](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)

* Using spliter, navigate site to retrieve Featured Image URL, including full-size .jpg image

--[Mars Facts](https://space-facts.com/mars/)

* Simple Pandas scrape to obtain table of facts about Mars

--[Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

* Navigate USGS site to click on the 4 images of Mars' Hemisheres by appending each image to a dictionary

#
# MongoDB and Flask App

* Convert .ipynb file into Python script called scrape_mars.py
* Create route to import .py file and call scrape function
* Store values in MongoDB as Python dictionary
* Create HTML template to store data in order to visualize on single page

# 

# Visiualizations


