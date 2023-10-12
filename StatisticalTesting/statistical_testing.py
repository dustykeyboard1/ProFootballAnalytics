'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality: Run statisitcal testing on data.
'''

import pandas as pd
from scipy.stats import chi2_contingency
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class StatisticalTesting:
    def __init__(self, team1_data = None, team2_data = None):
        self.team1_data = None
        self.team2_data = None
        if team1_data:
            self.team1_data = pd.read_csv(team1_data)
        if team2_data:
            self.team2_data = pd.read_csv(team2_data)

        self.preprocess_data()

    def preprocess_data(self):
        '''
        Prepare data for statistical testing.
        '''
        # Remove rows where games haven't been played yet
        self.team1_data = self.team1_data[self.team1_data['points_for'] != 0]
        if self.team2_data is not None:
            self.team2_data = self.team2_data[self.team2_data['points_for'] != 0]
        
        # Convert 'rest_days' to integer
        self.team1_data['rest_days'] = self.team1_data['rest_days'].str.extract('(\d+)').astype(int)
        if self.team2_data is not None:
            self.team2_data['rest_days'] = self.team2_data['rest_days'].str.extract('(\d+)').astype(int)

        
        
        # One-hot encode 'day' and 'opp' columns
        self.team1_data = pd.get_dummies(self.team1_data, columns=['day', 'opp'])
        if self.team2_data is not None:
            self.team2_data = pd.get_dummies(self.team2_data, columns=['day', 'opp'])

        # Columns to shift up
        shift_columns = ['points_for', 'points_allowed', 'tot_yds', 'pass_yds', 'rush_yds', 'opp_tot_yds', 'opp_pass_yds', 'opp_rush_yds']
        
        # Shift up the columns for team 1 and team 2
        self.team1_data[shift_columns] = self.team1_data[shift_columns].shift(-1)
        if self.team2_data is not None:
            self.team2_data[shift_columns] = self.team2_data[shift_columns].shift(-1)
        
        # Drop the last row as it will have NaNs after shifting
        self.team1_data.drop(self.team1_data.tail(1).index, inplace=True)
        if self.team2_data is not None:
            self.team2_data.drop(self.team2_data.tail(1).index, inplace=True)

        # Make sure both dataframes have the same columns
        # Convert the set to a list
        if self.team2_data:
            common_cols = list(set(self.team1_data.columns) & set(self.team2_data.columns))
            common_cols = [col for col in common_cols if 'opp' not in col]
            self.team1_data = self.team1_data[common_cols]
            self.team2_data = self.team2_data[common_cols]
        


    def moneyline_logistic_regression(self, both_teams = True):
        # Prepare the data
        if self.team2_data and both_teams:
            X = pd.concat([self.team1_data, self.team2_data])
            y = X['result'].apply(lambda x: 1 if x == 'W' else 0)
            X = X.drop(['result'], axis=1)
        else:
            X = self.team1_data
            y = X['result'].apply(lambda x: 1 if x == 'W' else 0)
            X = X.drop(['result'], axis=1)

        if X.isnull().values.any():
            print("Warning: NaN values found. Filling with zeros.")
            raise ValueError("Found NaN values.")

        # Initialize the model
        model = LogisticRegression()
        model = LogisticRegression(max_iter=1000)

        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(X)

        # Fit the model
        model.fit(self.X_scaled, y)
        

        # Get the odds ratio
        odds_ratio = pd.DataFrame({'feature': X.columns, 'odds_ratio': np.exp(model.coef_[0])})
        filtered_odds_ratio = odds_ratio[odds_ratio['odds_ratio'] > 1]

        # Visualization
        plt.figure(figsize=(10, 6))
        plt.barh(filtered_odds_ratio['feature'], filtered_odds_ratio['odds_ratio'])
        plt.xlabel('Odds Ratio')
        plt.ylabel('Feature')
        plt.title('Impact of Features on MoneyLine')
        plt.tight_layout()
        plt.show()

        return odds_ratio
    
    def run_chi_squared_test(self, team = 1):
        team_data = getattr(self, f'team{team}_data')
        contingency_table = pd.crosstab(team_data['home_team'], team_data['result'])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        print(f'Team{team}')
        print()
        print('Home Field Advantage:')
        if p < 0.05:
            print("Variables are dependent (reject H0)")
        else:
            print("Variables are independent (fail to reject H0)")

        contingency_table = pd.crosstab(team_data['rest_days'], team_data['result'])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        print()
        print('Rest Days:')
        if p < 0.05:
            print("Variables are dependent (reject H0)")
        else:
            print("Variables are independent (fail to reject H0)")






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
    
    def print_data(self):
        print(self.team1_data)
        print(self.team2_data)