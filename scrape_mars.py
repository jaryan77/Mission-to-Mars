from splinter import Browser
from bs4 import BeautifulSoup
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser("chrome", **executable_path, headless=False)

    # news_t, news_p = news(browser)

    # listings = {
    #     "article":news_t,
    #     "paragraph":news_p,
    #     "featured_img":feat_img(browser),
    #     "mars_facts":fact_page(),
    #     "mars_hemi":mars_hemispheres(browser)
    # }

def scrape():
    browser = init_browser
    scrape_dict = {}
    # browser.quit()
    # return listings

# def news(browser):
#News article
    
    #Define url to scrape
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Retrieve latest article header and teaser
    news_t=soup.select_one('ul.item_list li.slide').find_all('div', class_='content_title')[0].text
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    
 

# def featured_img(browser):
#Featured image
    #Define url to scrape
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    full_image = browser.find_by_css('button.btn.btn-outline-light')
    # full_image.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    img_url_rel = img_soup.select_one('div.fancybox-inner img').get("src")
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    browser.visit(featured_image_url)
    # return featured_image_url

# def mars_facts(browser):
#Mars Facts
    facts_url='https://space-facts.com/mars/'
    tables=pd.read_html(facts_url)
    facts = tables[0]
    facts = facts.rename(columns={0:'Fact',1:'Measurement'})
    facts
    mars_table = facts.to_html()
    mars_table.replace('\n','')

#Hemisphere Shots
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_image_urls = []
    links = browser.find_by_css('a.product-item h3')

    for i in range(len(links)):
        hemi_dict = {}
        browser.find_by_css('a.product-item h3')[i].click()
        hemi_dict['title'] = browser.find_by_css('h2.title').text
        cerberus_rel = browser.find_by_text('Sample')
        cerberus_rel.click()
        hemi_dict['img_url'] = cerberus_rel['href']
        hemisphere_image_urls.append(hemi_dict)
        # browser.back()

    hemisphere_image_urls    

scrape_dict = {
    "news_t":news_t,
    "news_p":news_p,
    "featured_image_url":featured_image_url,
    "mars_table":mars_table,
    "hemisphere_image_urls":hemisphere_image_urls
}

