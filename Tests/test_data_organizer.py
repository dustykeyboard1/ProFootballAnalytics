'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Create bigger data sets for each team.
'''
import sys
import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
root_dir += '/ProFootballAnalytics'
sys.path.append(root_dir)
from WebScraper.web_scraper import WebScraper
from StatisticalTesting.statistical_testing import StatisticalTesting


def main():
    team1 = "Kansas City Chiefs"
    team2 = "Denver Broncos"
    qb1 = "Patrick Mahomes"
    qb2 = 'Russell Wilson'
    year = 2022

    scraper = WebScraper(team1=team1, team2=team2, qb1=qb1, qb2=qb2, year=year)
    path = scraper.fetch_and_save_historical_data(team = 2, start = 2010, end = 2023)
    print(f"Path returned: {path}")
    testsuite = StatisticalTesting(team1_data = path)
    testsuite.run_chi_squared_test()
    testsuite.moneyline_logistic_regression(both_teams=False)
main()