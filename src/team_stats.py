import pandas as pd

class TeamStats:
    def __init__(self, team_data: pd.DataFrame):
        self.team_data = team_data

    def get_team_results(self):
        wins = self.team_data[self.team_data['result'] == 'win'].shape[0]
        losses = self.team_data[self.team_data['result'] == 'loss'].shape[0]
        return {"wins": wins, "losses": losses}

    def get_team_composition(self):
        latest_match = self.team_data.iloc[-1]
        composition = latest_match['team_members']
        return composition

    def get_hero_picks(self):
        hero_picks = self.team_data['hero_picks'].explode().value_counts()
        return hero_picks.to_dict()