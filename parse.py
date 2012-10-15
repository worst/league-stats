import json
from models import *
from datetime import datetime
import re


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
        self.json_string = re.search("\{.*\}", self.replay.readline()).group()
        self.replay_data = json.loads(self.json_string)

    def process_replay_data(self):
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

    def parse_team_info(self):
        self.team1 = Team(side=Side.get_by(color=1),
                          game=self.new_game)
        self.team2 = Team(side=Side.get_by(color=2),
                          game=self.new_game)

        for player in self.replay_data['players']:
            summoner = Summoner.get_by(summoner_id=player['accountID'])
            champion = Champion.get_by(name=player['champion'])
            win_count = 1 if player['won'] == 'true' else 0
            loss_count = 1 if player['won'] == 'false' else 0
            summoner_stats = Summoner_Stats.get_by(summoner=summoner, champion=champion)

            if summoner == None:
                summoner = Summoner(summoner_id=player['accountID'],
                                    summoner_name=player['summoner'],
                                    wins=win_count,
                                    losses=loss_count)
            else:
                summoner.wins += win_count
                summoner.losses += loss_count

            if summoner_stats == None:
                Summoner_Stats(summoner=summoner, champion=champion, wins=win_count, losses=loss_count)
            else:
                summoner_stats.wins += win_count
                summoner_stats += loss_count

            if player['team'] == 1:
                self.team1.summoners.append(summoner)
                self.team1.champions.append(champion)
            else:
                self.team2.summoners.append(summoner)
                self.team2.champions.append(champion)
