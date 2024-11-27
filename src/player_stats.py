import pandas as pd
import matplotlib.pyplot as plt


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

    def generate_report(self):
        stats = self.get_player_stats()
        hero_performance = self.get_player_hero_performance()

        report = {
            "Player Stats": stats,
            "Hero Performance": hero_performance
        }
        return report

    def plot_kda(self):
        stats = self.get_player_stats()
        categories = list(stats.keys())
        values = list(stats.values())

        plt.figure(figsize=(8, 6))
        plt.bar(categories, values, color=['green', 'red', 'blue'])
        plt.xlabel('Metric')
        plt.ylabel('Average Value')
        plt.title('Player KDA Stats')
        plt.show()

    def plot_hero_performance(self):
        performance = self.get_player_hero_performance()
        heroes = list(performance.keys())
        gpm = [performance[hero]['gpm'] for hero in heroes]
        xpm = [performance[hero]['xpm'] for hero in heroes]

        plt.figure(figsize=(10, 6))
        plt.bar(heroes, gpm, color='gold', label='GPM')
        plt.bar(heroes, xpm, color='purple', label='XPM', bottom=gpm)
        plt.xlabel('Heroes')
        plt.ylabel('Gold/XP per Minute')
        plt.title('Player Hero Performance')
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
