import unittest
import pandas as pd
from src.player_stats import PlayerStats

class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        data = {
            'match_id': [1, 2, 3],
            'hero': ['HeroA', 'HeroB', 'HeroA'],
            'kills': [10, 7, 15],
            'deaths': [2, 4, 3],
            'assists': [8, 10, 12],
            'gpm': [500, 450, 550],
            'xpm': [600, 520, 580]
        }
        self.player_data = pd.DataFrame(data)
        self.player_stats = PlayerStats(self.player_data)

    def test_get_player_stats(self):
        stats = self.player_stats.get_player_stats()
        expected_stats = {
            "average_kills": 10.67,
            "average_deaths": 3.0,
            "average_assists": 10.0
        }
        for key in expected_stats:
            self.assertAlmostEqual(stats[key], expected_stats[key], places=2)

    def test_get_player_hero_performance(self):
        performance = self.player_stats.get_player_hero_performance()
        expected_performance = {
            'HeroA': {'gpm': 525.0, 'xpm': 590.0},
            'HeroB': {'gpm': 450.0, 'xpm': 520.0}
        }
        self.assertEqual(performance, expected_performance)

if __name__ == '__main__':
    unittest.main()