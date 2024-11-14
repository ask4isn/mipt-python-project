import pandas as pd
import matplotlib.pyplot as plt

class HeroTrends:
    def __init__(self, hero_data: pd.DataFrame):
        self.hero_data = hero_data

    def analyze_hero_picks(self):
        hero_picks = self.hero_data['hero'].value_counts()
        return hero_picks.to_dict()

    def analyze_hero_combinations(self):
        combinations = self.hero_data.groupby('match_id')['hero'].apply(lambda x: tuple(sorted(x))).value_counts()
        return combinations.to_dict()

    def generate_report(self):
        hero_picks = self.analyze_hero_picks()
        hero_combinations = self.analyze_hero_combinations()

        report = {
            "Popular Hero Picks": hero_picks,
            "Hero Combinations": hero_combinations
        }
        return report

    def plot_hero_popularity(self):
        hero_picks = self.analyze_hero_picks()
        heroes = list(hero_picks.keys())
        counts = list(hero_picks.values())

        plt.figure(figsize=(10, 6))
        plt.bar(heroes, counts)
        plt.xlabel('Heroes')
        plt.ylabel('Pick Frequency')
        plt.title('Hero Popularity')
        plt.xticks(rotation=45)
        plt.show()

    def plot_hero_combinations(self):
        combinations = self.analyze_hero_combinations()
        combo_names = [', '.join(combo) for combo in combinations.keys()]
        counts = list(combinations.values())

        plt.figure(figsize=(12, 6))
        plt.bar(combo_names, counts)
        plt.xlabel('Hero Combinations')
        plt.ylabel('Frequency')
        plt.title('Popular Hero Combinations')
        plt.xticks(rotation=90)
        plt.show()
