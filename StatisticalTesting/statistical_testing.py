'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Run statisitcal testing on data.
'''

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

class StatisticalTesting:
    def __init__(self, team1_data, team2_data):
        self.team1_data = pd.read_csv(team1_data)
        self.team2_data = pd.read_csv(team2_data)

    def moneyline_logistic_regression(self):
        # Prepare the data
        X = pd.concat([self.team1_data, self.team2_data])
        y = X['result'].apply(lambda x: 1 if x == 'W' else 0)
        X = X.drop(['result'], axis=1)

        # Initialize the model
        model = LogisticRegression()

        # Fit the model
        model.fit(X, y)

        # Get the odds ratio
        odds_ratio = pd.DataFrame({'feature': X.columns, 'odds_ratio': np.exp(model.coef_[0])})

        # Visualization
        plt.figure(figsize=(10, 6))
        plt.barh(odds_ratio['feature'], odds_ratio['odds_ratio'])
        plt.xlabel('Odds Ratio')
        plt.ylabel('Feature')
        plt.title('Impact of Features on MoneyLine')
        plt.show()

        return odds_ratio

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