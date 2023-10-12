'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality:
Create a class called 'WebScraper' to scrape, parse and store data from
the ProFootballReference website.
'''

from pro_football_reference_web_scraper import player_game_log, player_splits, team_game_log, team_splits
import json
import pandas as pd

class WebScraper:
    def __init__(self, team1, team2, qb1, qb2, config_file='WebScraper/config.json', year=2023):
        self.team1 = team1
        self.team2 = team2
        self.team1qb = qb1
        self.team2qb = qb2
        self.parsed_data = None
        self.year = year

    def fetch_data(self, team = False, QB = False):
        if team: 
            self.team1_data = team_game_log.get_team_game_log(team=self.team1, season=self.year)
            self.team2_data = team_game_log.get_team_game_log(team=self.team2, season=self.year)
        if QB:
            self.team1_qb_data = player_game_log.get_player_game_log(player = self.team1qb, position='QB', season=self.year)
            self.team2_qb_data = player_game_log.get_player_game_log(player = self.team2qb, position='QB', season=self.year)

    def parse_data(self):
        # You can add your parsing logic here, if needed
        pass

    def save_data(self, file_name='temp_data.json', team = False, QB = False):
        if team: 
            self.team1_data.to_csv(f'DataOrganizer/{self.team1}_team_data.csv', index=False)
            self.team2_data.to_csv(f'DataOrganizer/{self.team2}_team_data.csv', index=False)
        if QB: 
            self.team1_qb_data.to_csv(f'DataOrganizer/{self.team1}_QB_data.csv', index=False)
            self.team2_qb_data.to_csv(f'DataOrganizer/{self.team2}_QB_data.csv', index=False)
        return f'DataOrganizer/{self.team1}_team_data.csv', f'DataOrganizer/{self.team2}_team_data.csv', f'DataOrganizer/{self.team1}_QB_data.csv', f'DataOrganizer/{self.team2}_QB_data.csv'

    def print_team_data(self):
        print(self.team1_data)
        print(self.team2_data)
    
    def fetch_and_save_historical_data(self, team = 1, start = None, end = None):
        '''
        Creates and saves historical data CSV from start to end.
        Params: Start - year to start
                End - year to end
        '''
        df = pd.DataFrame(columns=['week','day','rest_days','home_team','distance_travelled','opp','result','points_for',
                                   'points_allowed', 'tot_yds','pass_yds','rush_yds','opp_tot_yds','opp_pass_yds',
                                   'opp_rush_yds'])
        for i in range(start, end + 1):
            if team == 1:
                temp_data = team_game_log.get_team_game_log(team=self.team1, season=i)
            else: 
                temp_data = team_game_log.get_team_game_log(team=self.team2, season=i)
            df = pd.concat([df, temp_data])
        
        if team == 1:
            df.to_csv(f'DataOrganizer/{self.team1}_historical_data.csv', index=False)
            print('Saved to CSV.')
            return f'DataOrganizer/{self.team1}_historical_data.csv'
        else:
            df.to_csv(f'DataOrganizer/{self.team2}_historical_data.csv', index=False)
            print('Saved to CSV.')
            return f'DataOrganizer/{self.team2}_historical_data.csv'