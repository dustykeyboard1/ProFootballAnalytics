'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Test the webscraping functionality.
'''
import sys
import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
root_dir += '/ProFootballAnalytics'
sys.path.append(root_dir)
from WebScraper.web_scraper import WebScraper

def main():
    scraper = WebScraper('nyg', 'mia')
    scraper.set_teams()
    scraper.fetch_data()


main()