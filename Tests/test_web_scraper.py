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
from StatisticalTesting.statistical_testing import StatisticalTesting

def main():
    team1 = "Buffalo Bills"
    team2 = "New York Jets"
    qb1 = "Josh Allen"
    qb2 = 'Zach Wilson'

    scraper = WebScraper(team1=team1, team2=team2, qb1=qb1, qb2=qb2)
    scraper.fetch_data()
    scraper.parse_data()
    team1csv, team2csv, qb1csv, qb2csv = scraper.save_data()

    StatisticalTesting(team1csv, team2csv)
    

main()