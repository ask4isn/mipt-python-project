import pandas as pd
import matplotlib.pyplot as plt

class TeamStats:
    def __init__(self, team_data: pd.DataFrame, place: int):
        self.team_data = team_data
        self.place = place

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

    def generate_report(self):
        results = self.get_team_results()
        hero_picks = self.get_hero_picks()

        report = {
            "Place": self.place,
            "Team Results": results,
            "Popular Hero Picks": hero_picks
        }
        return report

    def plot_results(self):
        results = self.get_team_results()
        labels = list(results.keys())
        sizes = list(results.values())

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Team Results: Wins vs Losses (Place: {self.place})')
        plt.show()

    def plot_hero_picks(self):
        hero_picks = self.get_hero_picks()
        heroes = list(hero_picks.keys())
        counts = list(hero_picks.values())

        plt.figure(figsize=(10, 6))
        plt.bar(heroes, counts)
        plt.xlabel('Heroes')
        plt.ylabel('Pick Count')
        plt.title('Hero Picks Frequency for Team')
        plt.xticks(rotation=45)
        plt.show()
