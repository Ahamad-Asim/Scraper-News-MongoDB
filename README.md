# Scraper-News-MongoDB
 This is a Scrapy script that crawls a specified news website and stores the scraped data in a MongoDB database. The script uses the Scrapy framework to navigate the website, extract the relevant information and store it in the specified MongoDB collection

This script is a web scraper that uses the Scrapy library to crawl a website and extract news articles and their summaries. The script creates a spider that starts at a specified URL and follows links to other pages within the allowed domains, using the LinkExtractor class to identify the relevant links. The spider then parses the pages, using CSS selectors to extract the title, summary, and name of the news articles, and saves the data to an item container.

## Usage

To use this script, you'll need to have Scrapy installed. You can install it by running `pip install scrapy`.

1. Replace `allowed_domains` and `start_urls` with the allowed domain and the link to start scraping.
2. Replace the css selectors in the parse_item function according to the site you want to scrape.
3. Run the script with `scrapy runspider NewsScraper.py`


Note that the script is set up to scrape the news articles and their summaries, but you can also modify the script to scrape other information from the website by adjusting the CSS selectors and the item container as needed.


## MongoDB
To store the data in mongodb

1. Edit the `settings.py` file. Uncomment the `ITEM PIPELINES`
2. Edit the `pipelines.py` file. 
3. Use `pymongo` to connect to Mongodb database 

An example `pipelines.py` script is given
<br>
<br>
The pipeline connects to a MongoDB database and stores items in a collection named 'politics' in a database named 'news'. The pipeline uses the pymongo library to establish a connection to a MongoDB instance running on the localhost on port 27017 and insert the data using the insert_one method.


## Dependency
This script uses `items.py` file which contains HiItem class. make sure you have that file in the same directory as the script.
it is used for storing the scraped data into containers



