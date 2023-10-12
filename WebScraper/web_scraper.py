'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality:
Create a class called 'WebScraper' to scrape, parse and store data from
the ProFootballReference website.
'''


import requests
import json 

class WebScraper:
    def __init__(self, config_file='config.json'):
        '''
        Initialize a new WebScraper
        Parameters: config_file - saved in the WebScraper Directory
        '''
        with open(config_file, 'r') as f:
            config = json.load(f)
        self.base_url = config['base_url']
        self.headers = config['headers']
        self.raw_data = None
        self.parsed_data = None
    
    def set_teams(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_url = f"{self.base_url}/{self.team1}"
        self.team2_url = f"{self.base_url}/{self.team2}"

    def fetch_data(self):
        self.raw_data = {}
        for team, url in {'team1': self.team1_url, 'team2': self.team2_url}.items():
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                self.raw_data[team] = response.text
            else:
                print(f"Failed to fetch data for {team}. Status code: {response.status_code}")


    def parse_data(self):
        pass

    def save_data(self, file_name='temp_data.json'):
        with open(file_name, 'w') as f:
            json.dump(self.parsed_data, f)