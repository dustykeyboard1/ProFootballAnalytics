'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Run the product
'''

from WebScraper.web_scraper import WebScraper

def main():
    scraper = WebScraper()
    scraper.set_teams('NY/2023.htm', 'MIA/2023.htm')
    scraper.fetch_data()