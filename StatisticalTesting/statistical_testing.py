'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Run statisitcal testing on data.
'''

import pandas as pd
from scipy import stats
import statsmodels.api as sm

class StatisticalTesting:
    def __init__(self, team1_data, team2_data):
        self.team1_data = pd.read_csv(team1_data)
        self.team2_data = pd.read_csv(team2_data)

    def run_t_test(self, column):
        # Implement T-Test here
        pass

    def run_anova(self, column):
        # Implement ANOVA here
        pass

    def run_correlation(self, column1, column2):
        # Implement Correlation here
        pass

    def run_logistic_regression(self, column):
        # Implement Logistic Regression here
        pass

# Example usage:
# stats_test = StatisticalTesting('team1_data.csv', 'team2_data.csv')
# stats_test.run_t_test('points_for')
# stats_test.run_anova('pass_yds')
# stats_test.run_correlation('pass_yds', 'points_for')
# stats_test.run_logistic_regression('result')