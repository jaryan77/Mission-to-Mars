from splinter import Browser
from bs4 import BeautifulSoup
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser("chrome", **executable_path, headless=False)



def news(browser):
#News article
    
    #Define url to scrape
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    #Retrieve latest article header and teaser
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text
    
    return news_title, news_p
 

def featured_img(browser):
#Featured image
    #Define url to scrape
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jpl_url)
    
    full_image = browser.find_by_css('button.btn.btn-outline-light')
    full_image.click()

    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    img_url_rel = img_soup.select_one('div.fancybox-inner img').get("src")
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    
    return featured_image_url

def mars_facts():
#Mars Facts
    facts_url='https://space-facts.com/mars/'
    
    tables=pd.read_html(facts_url)
    facts = tables[0]
    facts = facts.rename(columns={0:'Fact',1:'Measurement'})
    
    mars_table = facts.to_html()
    return mars_table
    
#Hemisphere Links
def hemisphere(browser):
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

    hemisphere_image_urls = []
    links = browser.find_by_css('a.product-item h3')

    for i in range(len(links)):
        hemi_dict = {}
        browser.find_by_css('a.product-item h3')[i].click()
        
        sample_hemi = browser.find_by_text('Sample').first
        
        hemi_dict['img_url'] = sample_hemi['href']          
        
        hemi_dict['title'] = browser.find_by_css('h2.title').text


        hemisphere_image_urls.append(hemi_dict)
        browser.back()

    return hemisphere_image_urls    

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    
    news_title ,news_p = news(browser)
    featured_image_url = featured_img(browser)
    mars_table = mars_facts()
    hemisphere_image_urls = hemisphere(browser)


    scrape_dict={
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_img" : featured_image_url,
        "mars_table" : mars_table,
        "hemisphere":hemisphere_image_urls
    }
    browser.quit()
    return scrape_dict
if __name__ == "__main__":
    print(scrape())