from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

    news_t, news_p = news(browser)

    listings = {
        "article":news_t,
        "paragraph":news_p,
        "featured_img":feat_img(browser),
        "mars_facts":fact_page(),
        "mars_hemi":mars_hemispheres(browser)
    }
    browser.quit()
    return listings

def news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_t=soup.select_one('ul.item_list li.slide').find_all('div', class_='content_title')[0].text
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    
    return news_t, news_p

def featured_img(browser):
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    full_image = browser.find_by_css('button.btn.btn-outline-light')
    full_image.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    img_url_rel = img_soup.select_one('div.fancybox-inner img').get("src")
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return featured_image_url