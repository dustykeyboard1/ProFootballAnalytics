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
    team1 = "min"
    team2 = "chi"
    qb1 = None
    qb2 = None
    year = 2023

    scraper = WebScraper(team1=team1, team2=team2, qb1=qb1, qb2=qb2, year=year)
    # path = scraper.fetch_and_save_historical_data(team = 2, start = 2010, end = 2023)
    # print(f"Path returned: {path}")
    scraper.fetch_data(rankings=True)
    _, _, _, _, team1_rankings, team2_reankings = scraper.save_data(rankings=True)

    testsuite = StatisticalTesting(team1, team2)
    testsuite.compare_important_features()
    testsuite.compare_additional_stats()
    # testsuite.run_chi_squared_test()
    # testsuite.moneyline_logistic_regression(both_teams=False)
    input("Press enter to close plots." + '\n')
main()