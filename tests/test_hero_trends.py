import unittest
import pandas as pd
from src.hero_trends import HeroTrends

class TestHeroTrends(unittest.TestCase):
    def setUp(self):
        data = {
            'match_id': [1, 1, 2, 2, 3, 3],
            'hero': ['HeroA', 'HeroB', 'HeroA', 'HeroC', 'HeroB', 'HeroC']
        }
        self.hero_data = pd.DataFrame(data)
        self.hero_trends = HeroTrends(self.hero_data)

    def test_analyze_hero_picks(self):
        hero_picks = self.hero_trends.analyze_hero_picks()
        expected_picks = {'HeroA': 2, 'HeroB': 2, 'HeroC': 2}
        self.assertEqual(hero_picks, expected_picks)

    def test_analyze_hero_combinations(self):
        hero_combinations = self.hero_trends.analyze_hero_combinations()
        expected_combinations = {
            ('HeroA', 'HeroB'): 1,
            ('HeroA', 'HeroC'): 1,
            ('HeroB', 'HeroC'): 1
        }
        self.assertEqual(hero_combinations, expected_combinations)

if __name__ == '__main__':
    unittest.main()