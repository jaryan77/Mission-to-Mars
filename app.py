# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    scrape_dict = mongo.db.scrape_dict.find_one()
    # Return template and data
    print(scrape_dict)
    return render_template("index.html", scrape_dict=scrape_dict)


@app.route("/scrape")
def scraper():
  
    scrape_dict = mongo.db.scrape_dict
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    scrape_dict.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)