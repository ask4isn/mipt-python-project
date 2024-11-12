import pandas as pd

class PlayerStats:
    def __init__(self, player_data: pd.DataFrame):
        self.player_data = player_data

    def get_player_stats(self):
        avg_kills = self.player_data['kills'].mean()
        avg_deaths = self.player_data['deaths'].mean()
        avg_assists = self.player_data['assists'].mean()
        return {
            "average_kills": avg_kills,
            "average_deaths": avg_deaths,
            "average_assists": avg_assists
        }

    def get_player_hero_performance(self):
        performance = self.player_data.groupby('hero')[['gpm', 'xpm']].mean()
        return performance.to_dict(orient='index')