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
    scraper = WebScraper(team1="Buffalo Bills", team2="New York Jets", qb1='Josh Allen', qb2='Zach Wilson')
    scraper.fetch_data()
    scraper.parse_data()
    scraper.save_data()
    # scraper.print_team_data()



main()