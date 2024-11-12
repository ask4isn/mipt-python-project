import pandas as pd

class HeroTrends:
    def __init__(self, hero_data: pd.DataFrame):
        self.hero_data = hero_data

    def analyze_hero_picks(self):
        hero_picks = self.hero_data['hero'].value_counts()
        return hero_picks.to_dict()

    def analyze_hero_combinations(self):
        combinations = self.hero_data.groupby('match_id')['hero'].apply(lambda x: tuple(sorted(x))).value_counts()
        return combinations.to_dict()