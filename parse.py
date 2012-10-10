import json
from models import *
from datetime import datetime


class UploadParser:
    replay = None
    replay_path = ''
    json_string = ''
    replay_data = None

    new_game = None
    team1 = None
    team2 = None

    def __init__(self, path):
        self.replay_path = path
        self.extract_json()

    def extract_json(self):
        self.replay = open(self.replay_path)
        self.json_string = self.replay.readline()[8:][:-58]
        self.replay_data = json.loads(self.json_string)

    def process_replay_data(self):
        self.parse_summoner_info()
        self.parse_game_info()
        self.parse_team_info()

        session.commit()

    def is_correct_game_mode(self):
        if "map" in self.replay_data and self.replay_data['map'] == 1:
            return True
        else:
            return False

    def parse_game_info(self):
        date = datetime.fromtimestamp(self.replay_data['timestamp'])
        length = self.replay_data['matchLength']
        winning_side = self.replay_data['winningTeam']

        self.new_game = Game(date=date,
                             length=length,
                             replay_path=self.replay_path,
                             winner=Side.get_by(color=winning_side))

    def parse_summoner_info(self):
        for player in self.replay_data['players']:
            if Summoner.get_by(summoner_id=player['accountID']) == None:
                Summoner(summoner_id=player['accountID'],
                         summoner_name=player['summoner'])

    def parse_team_info(self):
        self.team1 = Team(side=Side.get_by(color=1),
                          game=self.new_game)
        self.team2 = Team(side=Side.get_by(color=2),
                          game=self.new_game)

        for player in self.replay_data['players']:
            if player['team'] == 1:
                self.team1.summoners.append(Summoner.get_by(summoner_id=player['accountID']))
                self.team1.champions.append(Champion.get_by(name=player['champion']))
            else:
                self.team2.summoners.append(Summoner.get_by(summoner_id=player['accountID']))
                self.team2.champions.append(Champion.get_by(name=player['champion']))
