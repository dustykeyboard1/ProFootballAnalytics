'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality:
Create a class called 'WebScraper' to scrape, parse and store data from
the ProFootballReference website.
'''

from pro_football_reference_web_scraper import player_game_log, player_splits, team_game_log, team_splits
import json

class WebScraper:
    def __init__(self, team1, team2, config_file='WebScraper/config.json'):
        with open(config_file, 'r') as f:
            config = json.load(f)
        self.team1 = team1
        self.team2 = team2
        self.parsed_data = None

    def fetch_data(self):
        self.team1_data = team_game_log.get_team_game_log(team=self.team1, season=2023)
        self.team2_data = team_game_log.get_team_game_log(team=self.team2, season=2023)

    def parse_data(self):
        # You can add your parsing logic here, if needed
        pass

    def save_data(self, file_name='temp_data.json'):
        with open(file_name, 'w') as f:
            json.dump(self.parsed_data, f)

    def print_team_data(self):
        print(self.team1_data)
        print(self.team2_data)