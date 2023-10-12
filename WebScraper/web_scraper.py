'''
Author: Michael Scoleri
Date: 10-12-2023
Functionality:
Create a class called 'WebScraper' to scrape, parse and store data from
the ProFootballReference website.
'''


import requests
import json 
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, team1, team2, config_file='WebScraper/config.json'):
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
        self.team1 = team1
        self.team2 = team2
    
    def set_teams(self):
        self.team1_url = f"{self.base_url}{self.team1}/2023.htm"
        self.team2_url = f"{self.base_url}{self.team2}/2023.htm"

    def fetch_data(self):
        self.team1_data = self._fetch_team_data(self.team1_url)
        self.team2_data = self._fetch_team_data(self.team2_url)

    def _fetch_team_data(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape Schedule & Game Results Table
        schedule_table = soup.find('table', {'id': 'games'})
        # Your code to scrape this table
        print(schedule_table)
        
        # Scrape Passing Table
        passing_table = soup.find('table', {'id': 'passing'})
        # Your code to scrape this table
        
        # Scrape Rushing & Receiving Table
        rushing_table = soup.find('table', {'id': 'rushing_and_receiving'})
        # Your code to scrape this table
        
        # Scrape Defense & Fumbles Table
        defense_table = soup.find('table', {'id': 'defense'})
        # Your code to scrape this table


    def parse_data(self):
        pass

    def save_data(self, file_name='temp_data.json'):
        with open(file_name, 'w') as f:
            json.dump(self.parsed_data, f)

    def print_team_urls(self):
        print(self.team1_url)
        print(self.team2_url)